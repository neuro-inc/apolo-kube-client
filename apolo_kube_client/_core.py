import asyncio
import json
import logging
import ssl
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager, suppress
from dataclasses import dataclass
from pathlib import Path
from ssl import SSLContext
from types import TracebackType
from typing import Self, TypeVar, cast

import aiohttp
import kubernetes
from aiohttp import ClientSession
from kubernetes.client import ApiClient
from yarl import URL, Query

from ._config import KubeClientAuthType, KubeConfig
from ._errors import (
    KubeClientException,
    KubeClientUnauthorized,
    ResourceBadRequest,
    ResourceExists,
    ResourceGone,
    ResourceInvalid,
    ResourceNotFound,
)
from ._typedefs import JsonType

logger = logging.getLogger(__name__)


_ERROR_CODES_MAPPING = {
    400: ResourceBadRequest,
    401: KubeClientUnauthorized,
    403: KubeClientException,
    404: ResourceNotFound,
    409: ResourceExists,
    410: ResourceGone,
    422: ResourceInvalid,
}

ModelT = TypeVar("ModelT")


@dataclass
class _KubeResponse:
    data: bytes


class _KubeCore:
    """
    Transport provider for Kube API client.

    Internal class.
    """

    def __init__(
        self,
        config: KubeConfig,
        *,
        http: ClientSession | None = None,
        trace_configs: list[aiohttp.TraceConfig] | None = None,
    ) -> None:
        self._base_url: URL = URL(config.endpoint_url)
        self._namespace = config.namespace
        self._forced_namespace = config.forced_namespace

        if config.auth_type == KubeClientAuthType.TOKEN:
            assert config.token or config.token_path
        elif config.auth_type == KubeClientAuthType.CERTIFICATE:
            assert config.auth_cert_path
            assert config.auth_cert_key_path

        self._auth_type = config.auth_type
        self._token = config.token
        self._token_path = config.token_path
        self._token_update_interval_s = config.token_update_interval_s
        self._ssl_context = self._create_ssl_context(config)

        self._conn_timeout_s = config.client_conn_timeout_s
        self._read_timeout_s = config.client_read_timeout_s
        self._watch_timeout_s = config.client_watch_timeout_s
        self._conn_pool_size = config.client_conn_pool_size
        self._trace_configs = trace_configs

        self._client: aiohttp.ClientSession | None = http
        self._http_supplied = http is not None
        self._token_updater_task: asyncio.Task[None] | None = None

        # Initialize the 3d party Official Kubernetes API client,
        # this is used only for deserialization raw responses for models
        self._api_client = ApiClient()

    def __str__(self) -> str:
        return self.__class__.__name__

    async def __aenter__(self) -> Self:
        await self.init()
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        await self.close()

    @property
    def http(self) -> ClientSession:
        assert self._client, "KubeClient must be initialized *prior* to getting `http`"
        return self._client

    async def init(self) -> None:
        logger.info("%s: initializing", self)
        if self._token_path:
            self._refresh_token_from_file()
            self._token_updater_task = asyncio.create_task(self._start_token_updater())

        if self._http_supplied:
            # http client was provided, no need to instantiate our own
            return

        connector = aiohttp.TCPConnector(limit=self._conn_pool_size)

        timeout = aiohttp.ClientTimeout(
            connect=self._conn_timeout_s, total=self._read_timeout_s
        )
        self._client = aiohttp.ClientSession(
            connector=connector,
            timeout=timeout,
            trace_configs=self._trace_configs,
            raise_for_status=self._raise_for_status,
        )

    async def close(self) -> None:
        logger.info("%s: closing", self)
        if self._client and not self._http_supplied:
            await self._client.close()
            self._client = None
        if self._token_updater_task:
            self._token_updater_task.cancel()
            with suppress(asyncio.CancelledError):
                await self._token_updater_task
            self._token_updater_task = None
        logger.info("%s: closed", self)

    @property
    def base_url(self) -> URL:
        return self._base_url

    @property
    def namespace(self) -> str:
        return self._namespace

    def resolve_namespace(self, namespace: str | None = None) -> str:
        return self._forced_namespace or namespace or self._namespace

    @property
    def _base_headers(self) -> dict[str, str]:
        headers = {"Accept": "application/json"}
        headers.update(self._auth_headers)
        return headers

    @property
    def _auth_headers(self) -> dict[str, str]:
        if self._auth_type != KubeClientAuthType.TOKEN or not self._token:
            return {}
        return {"Authorization": f"Bearer {self._token}"}

    @staticmethod
    async def _raise_for_status(response: aiohttp.ClientResponse) -> None:
        if response.status >= 400:
            payload = await response.text()
            exc_cls = _ERROR_CODES_MAPPING.get(response.status, KubeClientException)
            raise exc_cls(payload)

    def _create_ssl_context(self, config: KubeConfig) -> SSLContext | bool:
        if self.base_url.scheme != "https":
            return False
        ssl_context = ssl.create_default_context(
            cafile=config.cert_authority_path,
            cadata=config.cert_authority_data_pem,
        )
        if config.auth_type == KubeClientAuthType.CERTIFICATE:
            ssl_context.load_cert_chain(
                config.auth_cert_path,  # type: ignore
                config.auth_cert_key_path,
            )
        return ssl_context

    async def _start_token_updater(self) -> None:
        """
        A task which periodically reads from the `token_path` and refreshes the token
        """
        if not self._token_path:
            logger.info("%s: token path does not exist. updater won't be started", self)
            return

        logger.info("%s: starting token updater task", self)

        while True:
            try:
                self._refresh_token_from_file()
            except Exception as exc:
                logger.exception("%s: failed to update kube token: %s", self, exc)
            await asyncio.sleep(self._token_update_interval_s)

    def _refresh_token_from_file(self) -> None:
        """Reads token from the file and updates a token value"""
        if not self._token_path:
            return
        token = Path(self._token_path).read_text().strip()
        if token == self._token:
            return
        self._token = token
        logger.info("%s: kube token was refreshed", self)

    def serialize(self, obj: ModelT) -> JsonType:
        return cast(JsonType, self._api_client.sanitize_for_serialization(obj))

    def deserialize(self, data: JsonType, klass: type[ModelT]) -> ModelT:
        kube_response = _KubeResponse(data=json.dumps(data).encode("utf-8"))
        return cast(ModelT, self._api_client.deserialize(kube_response, klass))

    async def deserialize_response(
        self,
        response: aiohttp.ClientResponse,
        klass: type[ModelT],
    ) -> ModelT:
        if not hasattr(kubernetes.client.models, klass.__name__):
            raise ValueError(f"Unsupported response type: {klass}")
        data = await response.read()
        kube_response = _KubeResponse(data=data)
        return cast(ModelT, self._api_client.deserialize(kube_response, klass))

    @asynccontextmanager
    async def request(
        self,
        method: str,
        url: URL | str,
        headers: dict[str, str] | None = None,
        params: Query = None,
        json: JsonType | None = None,
    ) -> AsyncIterator[aiohttp.ClientResponse]:
        """
        Context manager.
        Basic method for making requests to the Kube API.
        Returns an aiohttp.ClientResponse object.
        """
        assert self._client, "client is not initialized"
        headers = headers or {}
        headers.update(self._base_headers)
        logger.debug(
            "making request to url=%s method=%s headers=%s params=%s json=%s",
            url,
            method,
            headers,
            params,
            json,
        )
        async with self._client.request(
            method=method,
            url=url,
            headers=headers,
            params=params,
            json=json,
            ssl=self._ssl_context,
        ) as resp:
            yield resp

    #########################################
    # Raw Kube API calls with JSON response #
    #########################################
    async def get(
        self,
        url: URL | str,
        params: Query = None,
        json: JsonType | None = None,
    ) -> JsonType:
        async with self.request(
            method="GET", url=url, params=params, json=json
        ) as resp:
            return cast(JsonType, await resp.json())

    async def post(
        self,
        url: URL | str,
        params: Query = None,
        json: JsonType | None = None,
    ) -> JsonType:
        async with self.request(
            method="POST", url=url, params=params, json=json
        ) as resp:
            return cast(JsonType, await resp.json())

    async def patch(
        self,
        url: URL | str,
        params: Query = None,
        json: JsonType | None = None,
    ) -> JsonType:
        async with self.request(
            method="PATCH", url=url, params=params, json=json
        ) as resp:
            return cast(JsonType, await resp.json())

    async def put(
        self,
        url: URL | str,
        params: Query = None,
        json: JsonType | None = None,
    ) -> JsonType:
        async with self.request(
            method="PUT", url=url, params=params, json=json
        ) as resp:
            return cast(JsonType, await resp.json())

    async def delete(
        self,
        url: URL | str,
        params: Query = None,
        json: JsonType | None = None,
    ) -> JsonType:
        async with self.request(
            method="DELETE", url=url, params=params, json=json
        ) as resp:
            return cast(JsonType, await resp.json())

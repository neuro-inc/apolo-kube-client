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
from aiohttp.hdrs import METH_DELETE, METH_GET, METH_PATCH, METH_POST, METH_PUT
from kubernetes.client import ApiClient
from pydantic import BaseModel
from yarl import URL, Query

from ._config import KubeClientAuthType, KubeConfig
from ._transport import KubeTransport
from ._typedefs import JsonType

logger = logging.getLogger(__name__)

ModelT = TypeVar("ModelT")


@dataclass
class _KubeResponse:
    data: bytes


class _KubeCore:
    """
    A kubernetes core API client wrapper.
    Contains generic logic for interacting with the concrete kube cluster,
    including the authentication, and request/response management.

    Internal class.
    """

    def __init__(
        self,
        config: KubeConfig,
        *,
        transport: KubeTransport,
    ) -> None:
        self._base_url: URL = URL(config.endpoint_url)
        self._namespace = config.namespace

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

        self._transport = transport
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

    async def init(self) -> None:
        logger.info("%s: initializing", self)
        if self._token_path:
            self._refresh_token_from_file()
            self._token_updater_task = asyncio.create_task(self._start_token_updater())

    async def close(self) -> None:
        logger.info("%s: closing", self)
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
        return namespace or self._namespace

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
        if isinstance(obj, BaseModel):
            # for crd resources we use pydantic models
            return cast(JsonType, obj.model_dump())
        return cast(JsonType, self._api_client.sanitize_for_serialization(obj))

    def deserialize(self, data: JsonType, klass: type[ModelT]) -> ModelT:
        if issubclass(klass, BaseModel):
            # for crd resources we use pydantic models
            return klass.model_validate(data)
        kube_response = _KubeResponse(data=json.dumps(data).encode("utf-8"))
        return cast(ModelT, self._api_client.deserialize(kube_response, klass))

    async def deserialize_response(
        self,
        response: aiohttp.ClientResponse,
        klass: type[ModelT],
    ) -> ModelT:
        if issubclass(klass, BaseModel):
            # for crd resources we use pydantic models
            data = await response.json()
            return klass.model_validate(data)
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
        headers = headers or {}
        headers.update(self._base_headers)
        async with self._transport.request(
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
            method=METH_GET, url=url, params=params, json=json
        ) as resp:
            return cast(JsonType, await resp.json())

    async def post(
        self,
        url: URL | str,
        params: Query = None,
        json: JsonType | None = None,
    ) -> JsonType:
        async with self.request(
            method=METH_POST, url=url, params=params, json=json
        ) as resp:
            return cast(JsonType, await resp.json())

    async def patch(
        self,
        url: URL | str,
        params: Query = None,
        json: JsonType | None = None,
    ) -> JsonType:
        async with self.request(
            method=METH_PATCH, url=url, params=params, json=json
        ) as resp:
            return cast(JsonType, await resp.json())

    async def put(
        self,
        url: URL | str,
        params: Query = None,
        json: JsonType | None = None,
    ) -> JsonType:
        async with self.request(
            method=METH_PUT, url=url, params=params, json=json
        ) as resp:
            return cast(JsonType, await resp.json())

    async def delete(
        self,
        url: URL | str,
        params: Query = None,
        json: JsonType | None = None,
    ) -> JsonType:
        async with self.request(
            method=METH_DELETE, url=url, params=params, json=json
        ) as resp:
            return cast(JsonType, await resp.json())

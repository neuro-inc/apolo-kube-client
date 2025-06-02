import asyncio
import logging
import ssl
from contextlib import suppress
from pathlib import Path
from typing import Any, Optional, Union

import aiohttp
from kubernetes import client
from yarl import URL

from ._config import KubeClientAuthType, KubeConfig
from ._errors import (
    KubeClientException,
    KubeClientExpired,
    KubeClientUnauthorized,
    ResourceBadRequest,
    ResourceExists,
    ResourceGone,
    ResourceInvalid,
    ResourceNotFound,
)

logger = logging.getLogger(__name__)


class _RESTResponse:
    """
    This is our custom analogue of the `kubernetes.client.rest.RESTResponse` class
    that is used for deserializing response data from the Kubernetes API.
    Aiohttp Response instead of the urllib3 Response
    """

    def __init__(self, resp: aiohttp.ClientResponse, data: bytes):
        self.response = resp
        self.status = resp.status
        self.reason = resp.reason
        self.data = data


class _KubeCore:
    """
    Transport provider for Kube API client.

    Internal class.
    """

    def __init__(
        self,
        config: KubeConfig,
        *,
        trace_configs: Optional[list[aiohttp.TraceConfig]] = None,
    ) -> None:
        self._base_url = config.endpoint_url
        self._namespace = config.namespace

        self._cert_authority_data_pem = config.cert_authority_data_pem
        self._cert_authority_path = config.cert_authority_path

        if config.auth_type == KubeClientAuthType.TOKEN:
            assert config.token or config.token_path, (
                "token or token path must be provided"
            )
        elif config.auth_type == KubeClientAuthType.CERTIFICATE:
            assert config.auth_cert_path and config.auth_cert_key_path, (
                "certs must be provided"
            )

        self._auth_type = config.auth_type
        self._auth_cert_path = config.auth_cert_path
        self._auth_cert_key_path = config.auth_cert_key_path
        self._token = config.token
        self._token_path = config.token_path
        self._token_update_interval_s = config.token_update_interval_s

        self._conn_timeout_s = config.client_conn_timeout_s
        self._read_timeout_s = config.client_read_timeout_s
        self._watch_timeout_s = config.client_watch_timeout_s
        self._conn_pool_size = config.client_conn_pool_size
        self._trace_configs = trace_configs

        self._client: Optional[aiohttp.ClientSession] = None
        self._token_updater_task: Optional[asyncio.Task[None]] = None

        # Initialize the 3d party Official Kubernetes API client,
        # this is used only for deserialization and its models
        self._api_client = client.ApiClient()

    def __str__(self) -> str:
        return self.__class__.__name__

    async def __aenter__(self) -> "_KubeCore":
        await self.init()
        return self

    async def __aexit__(self, *args: Any) -> None:
        await self.close()

    async def init(self) -> None:
        logger.info("%s: initializing", self)
        if self._token_path:
            self._refresh_token_from_file()
            self._token_updater_task = asyncio.create_task(self._start_token_updater())

        connector = aiohttp.TCPConnector(
            limit=self._conn_pool_size, ssl=self._create_ssl_context()
        )
        timeout = aiohttp.ClientTimeout(
            connect=self._conn_timeout_s, total=self._read_timeout_s
        )
        self._client = aiohttp.ClientSession(
            connector=connector,
            timeout=timeout,
            trace_configs=self._trace_configs,
        )

    async def close(self) -> None:
        logger.info("%s: closing", self)
        if self._client:
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

    async def request(
        self,
        *args: Any,
        raise_for_status: bool = True,
        response_type: Any = None,
        **kwargs: Any,
    ) -> Any:
        assert self._client, "client is not initialized"
        headers = kwargs.pop("headers", {}) or {}
        headers.update(self._auth_headers)  # populate auth (if exists)

        async with self._client.request(*args, headers=headers, **kwargs) as response:
            payload = await response.json()
            logger.debug("%s: k8s response payload: %s", self, payload)
            if raise_for_status:
                self._raise_for_status(payload)
            if response_type:
                rest_response = _RESTResponse(response, await response.read())
                return self._api_client.deserialize(rest_response, response_type)
            return payload

    async def get(self, *args: Any, **kwargs: Any) -> Any:
        return await self.request("GET", *args, **kwargs)

    async def post(self, *args: Any, **kwargs: Any) -> Any:
        return await self.request("POST", *args, **kwargs)

    async def patch(self, *args: Any, **kwargs: Any) -> Any:
        return await self.request("PATCH", *args, **kwargs)

    async def put(self, *args: Any, **kwargs: Any) -> Any:
        return await self.request("PUT", *args, **kwargs)

    async def delete(self, *args: Any, **kwargs: Any) -> Any:
        return await self.request("DELETE", *args, **kwargs)

    @property
    def _auth_headers(self) -> dict[str, Any]:
        if self._auth_type != KubeClientAuthType.TOKEN or not self._token:
            return {}
        return {"Authorization": f"Bearer {self._token}"}

    @staticmethod
    def _raise_for_status(payload: dict[str, Any]) -> None:
        kind = payload.get("kind")
        if kind == "Status":
            if payload.get("status") == "Success":
                return
            code = payload.get("code")
            reason = payload.get("reason")
            if reason == "Expired":
                raise KubeClientExpired(payload)
            if code == 400:
                raise ResourceBadRequest(payload)
            if code == 401:
                raise KubeClientUnauthorized(payload)
            if code == 404:
                raise ResourceNotFound(payload)
            if code == 409:
                raise ResourceExists(payload)
            if code == 410:
                raise ResourceGone(payload)
            if code == 422:
                raise ResourceInvalid(payload["message"])
            raise KubeClientException(payload["message"])

    @property
    def _is_ssl(self) -> bool:
        return self.base_url.scheme == "https"

    def _create_ssl_context(self) -> Union[ssl.SSLContext, bool]:
        if not self._is_ssl:
            return False
        ssl_context = ssl.create_default_context(
            cafile=self._cert_authority_path, cadata=self._cert_authority_data_pem
        )
        if self._auth_type == KubeClientAuthType.CERTIFICATE:
            ssl_context.load_cert_chain(
                self._auth_cert_path,  # type: ignore
                self._auth_cert_key_path,
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
            except asyncio.CancelledError:
                raise
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

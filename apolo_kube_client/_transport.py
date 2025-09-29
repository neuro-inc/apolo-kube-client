from __future__ import annotations

import logging
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from ssl import SSLContext
from types import TracebackType
from typing import Self

import aiohttp
from aiohttp import ClientSession
from yarl import URL, Query

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


ERROR_CODES_MAPPING: dict[int, type[Exception]] = {
    400: ResourceBadRequest,
    401: KubeClientUnauthorized,
    403: KubeClientException,
    404: ResourceNotFound,
    409: ResourceExists,
    410: ResourceGone,
    422: ResourceInvalid,
}


class KubeTransport:
    """
    Manages the underlying HTTP transport,
    providing the default error handling, timeout logic, etc.
    Can be used with multiple kubernetes clusters.
    """

    def __init__(
        self,
        *,
        conn_pool_size: int = 100,
        conn_timeout_s: int = 300,
        read_timeout_s: int = 300,
        trace_configs: list[aiohttp.TraceConfig] | None = None,
    ) -> None:
        self._session: ClientSession | None = None
        self._conn_pool_size = conn_pool_size
        self._conn_timeout_s = conn_timeout_s
        self._read_timeout_s = read_timeout_s
        self._trace_configs = trace_configs

    async def __aenter__(self) -> Self:
        connector = aiohttp.TCPConnector(limit=self._conn_pool_size)
        timeout = aiohttp.ClientTimeout(
            connect=self._conn_timeout_s, total=self._read_timeout_s
        )
        self._session = aiohttp.ClientSession(
            connector=connector,
            timeout=timeout,
            trace_configs=self._trace_configs,
            raise_for_status=self._raise_for_status,
        )
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        await self.session.close()

    @property
    def session(self) -> ClientSession:
        assert self._session is not None, "transport is not initialized"
        return self._session

    @staticmethod
    async def _raise_for_status(response: aiohttp.ClientResponse) -> None:
        if response.status >= 400:
            payload = await response.text()
            exc_cls = ERROR_CODES_MAPPING.get(response.status, KubeClientException)
            raise exc_cls(payload)

    @asynccontextmanager
    async def request(
        self,
        *,
        method: str,
        url: URL | str,
        headers: dict[str, str] | None = None,
        params: Query = None,
        json: JsonType | None = None,
        ssl: SSLContext | bool = False,
    ) -> AsyncIterator[aiohttp.ClientResponse]:
        logger.debug(
            "making request to url=%s method=%s headers=%s params=%s json=%s",
            url,
            method,
            headers,
            params,
            json,
        )
        async with self.session.request(
            method=method,
            url=url,
            headers=headers,
            params=params,
            json=json,
            ssl=ssl,
        ) as resp:
            yield resp

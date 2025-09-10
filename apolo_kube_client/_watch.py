import json
import logging
from collections.abc import AsyncIterator, Callable, Mapping
from contextlib import AbstractAsyncContextManager
from dataclasses import dataclass
from json import JSONDecodeError
from typing import TYPE_CHECKING, Any, Literal, NoReturn, Protocol

import aiohttp

from ._core import _ERROR_CODES_MAPPING
from ._errors import (
    KubeClientException,
    ResourceGone,
)
from ._typedefs import JsonType

if TYPE_CHECKING:
    from ._base_resource import KubeResourceModel


LOGGER = logging.getLogger(__name__)


@dataclass(frozen=True)
class WatchEvent[ModelT: KubeResourceModel]:
    type: Literal["ADDED", "MODIFIED", "DELETED"]
    object: ModelT


@dataclass(frozen=True)
class BookmarkEvent:
    resource_version: str


class GetResponse(Protocol):
    def __call__(
        self, resource_version: str | None
    ) -> AbstractAsyncContextManager[aiohttp.ClientResponse]: ...


class Watch[ModelT: KubeResourceModel]:
    def __init__(
        self,
        resource_version: str | None,
        get_response: GetResponse,
        deserialize: Callable[[JsonType], ModelT],
    ) -> None:
        self._resource_version = resource_version
        self._get_response = get_response
        self._deserialize = deserialize

    async def stream(self) -> AsyncIterator[WatchEvent[ModelT]]:
        # Initially True to avoid sending two requests at the start
        # if resource_version has already expired.
        is_retry_after_410 = True

        while True:
            try:
                async with self._get_response(
                    resource_version=self._resource_version
                ) as response:
                    await self._raise_for_status(response)

                    async for event in self._stream_from_response(response):
                        is_retry_after_410 = False

                        match event:
                            case BookmarkEvent():
                                self._resource_version = event.resource_version
                                continue
                            case _:
                                yield event
            except TimeoutError:
                pass
            except ResourceGone:
                if is_retry_after_410:
                    break
                is_retry_after_410 = True

    async def _stream_from_response(
        self, response: aiohttp.ClientResponse
    ) -> AsyncIterator[WatchEvent[ModelT] | BookmarkEvent]:
        async for line in response.content:
            if not line or line.isspace():
                continue
            try:
                event = json.loads(line)

                match event["type"]:
                    case "ERROR":
                        self._raise_for_error_event(event["object"])
                    case "BOOKMARK":
                        yield BookmarkEvent(
                            resource_version=event["object"]["metadata"][
                                "resourceVersion"
                            ]
                        )
                    case _:
                        yield WatchEvent(
                            type=event["type"],
                            object=self._deserialize(event["object"]),
                        )
            except JSONDecodeError:
                continue

    async def _raise_for_status(
        self, response: aiohttp.ClientResponse
    ) -> NoReturn | None:
        if response.ok:
            return None
        payload = await response.text()
        exc_cls = _ERROR_CODES_MAPPING.get(response.status, KubeClientException)
        raise exc_cls(payload)

    def _raise_for_error_event(self, payload: Mapping[str, Any]) -> NoReturn:
        exc_cls = _ERROR_CODES_MAPPING.get(payload["code"], KubeClientException)
        raise exc_cls(payload)

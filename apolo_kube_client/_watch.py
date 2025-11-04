import json
import logging
from collections.abc import AsyncGenerator, Callable
from contextlib import AbstractAsyncContextManager, aclosing
from dataclasses import dataclass
from json import JSONDecodeError
from typing import TYPE_CHECKING, Literal, NoReturn, Protocol

import aiohttp

from ._errors import ResourceGone, _raise_for_text, _raise_for_obj
from ._typedefs import JsonType

if TYPE_CHECKING:
    from ._models.base import ResourceModel


LOGGER = logging.getLogger(__name__)


@dataclass(frozen=True)
class WatchEvent[ModelT: ResourceModel]:
    type: Literal["ADDED", "MODIFIED", "DELETED"]
    object: ModelT


@dataclass(frozen=True)
class BookmarkEvent:
    resource_version: str


class GetResponse(Protocol):
    def __call__(
        self, resource_version: str | None
    ) -> AbstractAsyncContextManager[aiohttp.ClientResponse]: ...


class Watch[ModelT: ResourceModel]:
    def __init__(
        self,
        resource_version: str | None,
        get_response: GetResponse,
        deserialize: Callable[[JsonType], ModelT],
    ) -> None:
        self._resource_version = resource_version
        self._get_response = get_response
        self._deserialize = deserialize

    async def stream(self) -> AsyncGenerator[WatchEvent[ModelT]]:
        # Initially True to avoid sending two requests at the start
        # if resource_version has already expired.
        is_retry_after_410 = True

        while True:
            try:
                async with self._get_response(
                    resource_version=self._resource_version
                ) as response:
                    await self._raise_for_status(response)

                    async with aclosing(
                        self._stream_from_response(response)
                    ) as event_stream:
                        async for event in event_stream:
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
    ) -> AsyncGenerator[WatchEvent[ModelT] | BookmarkEvent]:
        async for line in response.content:
            if not line or line.isspace():
                continue
            try:
                event = json.loads(line)

                match event["type"]:
                    case "ERROR":
                        _raise_for_obj(event["object"])
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
        _raise_for_text(response.status, payload)

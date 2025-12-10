import logging
from collections.abc import Awaitable, Callable
from types import TracebackType
from typing import Self

from apolo_events_client import EventsClient, EventType, RecvEvent, StreamType


logger = logging.getLogger(__name__)


class EventsPoller:
    PLATFORM_VCLUSTER_STREAM = StreamType("platform-vcluster")
    EVENT_VCLUSTER_READY = EventType("vcluster-ready")

    def __init__(
        self,
        events_client: EventsClient,
        on_vcluster_ready: Callable[[RecvEvent], Awaitable[None]],
    ) -> None:
        self._events_client = events_client
        self._on_vcluster_ready = on_vcluster_ready

    async def __aenter__(self) -> Self:
        logger.info("Subscribe for %r", self.PLATFORM_VCLUSTER_STREAM)
        await self._events_client.subscribe_group(
            self.PLATFORM_VCLUSTER_STREAM,
            self._handler,
            auto_ack=True,
        )
        logger.info("Subscribed")
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        return exc_type is None

    async def _handler(self, ev: RecvEvent):
        logger.info("got event: %s", ev)
        match ev.event_type:
            case self.EVENT_VCLUSTER_READY:
                await self._on_vcluster_ready(ev)
            case _:
                logger.info("unsupported event")

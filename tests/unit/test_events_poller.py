from __future__ import annotations

from datetime import UTC, datetime
from unittest.mock import AsyncMock

from apolo_events_client import EventType, RecvEvent, StreamType

from apolo_kube_client._vcluster._poller import EventsPoller


async def test_events_poller_subscribes_on_enter() -> None:
    events_client = AsyncMock()
    on_ready = AsyncMock()

    async with EventsPoller(events_client=events_client, on_vcluster_ready=on_ready):
        pass

    events_client.subscribe_group.assert_awaited_once()
    args, kwargs = events_client.subscribe_group.await_args
    assert args[0] == EventsPoller.PLATFORM_VCLUSTER_STREAM
    # second arg is the handler callback
    assert callable(args[1])
    assert kwargs.get("auto_ack") is True


async def test_events_poller_calls_handler_for_vcluster_ready() -> None:
    on_ready = AsyncMock()
    events_client = AsyncMock()
    poller = EventsPoller(events_client=events_client, on_vcluster_ready=on_ready)

    event = RecvEvent(
        tag="t1",
        timestamp=datetime.now(UTC),
        sender="test",
        stream=StreamType("platform-vcluster"),
        event_type=EventType("vcluster-ready"),
        org="org",
        project="proj",
    )

    await poller._handler(event)

    on_ready.assert_awaited_once_with(event)


async def test_events_poller_ignores_unrelated_events() -> None:
    on_ready = AsyncMock()
    events_client = AsyncMock()

    poller = EventsPoller(events_client=events_client, on_vcluster_ready=on_ready)

    event = RecvEvent(
        tag="t1",
        timestamp=datetime.now(UTC),
        sender="test",
        stream=StreamType("platform-vcluster"),
        event_type=EventType("unrelated"),
        org="org",
        project="proj",
    )

    await poller._handler(event)

    on_ready.assert_not_awaited()

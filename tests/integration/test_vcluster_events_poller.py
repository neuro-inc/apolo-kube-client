from __future__ import annotations

from collections.abc import Callable
from datetime import UTC, datetime
from unittest.mock import AsyncMock

from apolo_events_client import EventsClient, EventType, RecvEvent, StreamType

from apolo_kube_client import KubeClientSelector, KubeConfig
from apolo_kube_client.apolo import generate_namespace_name


async def test_selector_with_events_client_subscribes_to_stream(
    kube_config: KubeConfig,
) -> None:
    async def fake_subscribe_group(
        stream: StreamType,
        handler: Callable[[RecvEvent], None],
        auto_ack: bool = True,
    ) -> None:
        subscribe_calls.append((stream, handler, auto_ack))

    subscribe_calls: list[tuple[StreamType, Callable[[RecvEvent], None], bool]] = []

    events_client = AsyncMock(spec=EventsClient)
    events_client.subscribe_group.side_effect = fake_subscribe_group

    async with KubeClientSelector(
        config=kube_config,
        events_client=events_client,
    ):
        # Ensure subscription happened with expected parameters.
        events_client.subscribe_group.assert_awaited()
        assert subscribe_calls
        stream, handler, auto_ack = subscribe_calls[0]
        assert stream == StreamType("platform-vcluster")
        assert callable(handler)
        assert auto_ack is True


async def test_vcluster_ready_event_triggers_cache_pop(
    kube_config: KubeConfig,
) -> None:
    captured_handler: list[Callable[[RecvEvent], None]] = []

    async def fake_subscribe_group(
        stream: StreamType,
        handler: Callable[[RecvEvent], None],
        auto_ack: bool = True,
    ) -> None:
        captured_handler.append(handler)

    events_client = AsyncMock(spec=EventsClient)
    events_client.subscribe_group.side_effect = fake_subscribe_group

    async with KubeClientSelector(
        config=kube_config,
        events_client=events_client,
    ) as selector:
        assert captured_handler, "EventsPoller did not register a handler"
        handler = captured_handler[0]

        selector._vcluster_cache.pop = AsyncMock(return_value=None)  # type: ignore[method-assign]

        org = "org"
        project = "proj"
        event = RecvEvent(
            tag="t1",  # type: ignore[arg-type]
            timestamp=datetime.now(UTC),
            sender="test",
            stream=StreamType("platform-vcluster"),
            event_type=EventType("vcluster-ready"),
            org=org,
            project=project,
        )

        await handler(event)  # type: ignore[misc]

        expected_key = generate_namespace_name(org, project)
        selector._vcluster_cache.pop.assert_awaited_once_with(expected_key)

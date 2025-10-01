from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from typing import Any
from unittest.mock import AsyncMock

import pytest
from aiohttp import ClientSession

from apolo_kube_client import KubeClient, KubeClientSelector, KubeConfig
from apolo_kube_client._errors import ResourceNotFound
from apolo_kube_client._transport import KubeTransport
from tests.unit.test_kube_client_selector import build_vcluster_secret


class _FakeResponse:
    async def json(self) -> dict[str, Any]:
        return {}


async def test_plain_clients_share_http_session(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    captured_ssl: list[Any] = []

    @asynccontextmanager
    async def fake_request(
        self: ClientSession, method: str, url: str, **kwargs: Any
    ) -> AsyncIterator[_FakeResponse]:
        captured_ssl.append(kwargs.get("ssl"))
        yield _FakeResponse()

    monkeypatch.setattr(ClientSession, "request", fake_request)

    cfg_a = KubeConfig(endpoint_url="https://k1.local")
    cfg_b = KubeConfig(endpoint_url="https://k2.local")

    async with KubeTransport() as transport:
        client_a = KubeClient(config=cfg_a, transport=transport)
        client_b = KubeClient(config=cfg_b, transport=transport)

        async with client_a, client_b:
            await client_a._core.get(url="https://a")
            await client_b._core.get(url="https://b")

    # same session handled both requests
    assert len(captured_ssl) == 2


async def test_selector_uses_shared_session(create_namespace_mock: AsyncMock) -> None:
    selector = KubeClientSelector(
        config=KubeConfig(endpoint_url="http://default.local")
    )

    secret = build_vcluster_secret(server="http://k1.local")
    selector._host_client.core_v1.secret.get = AsyncMock(  # type: ignore[method-assign]
        side_effect=[ResourceNotFound(), secret]
    )

    try:
        async with selector:
            async with selector.get_client(org_name="o1", project_name="p1") as c1:
                assert c1._origin._core._ssl_context is False

            async with selector.get_client(org_name="o2", project_name="p2") as c2:
                assert c2._origin._core._ssl_context is False

                # Same underlying transport reused
                assert c2._origin._transport is c1._origin._transport
    finally:
        await selector.aclose()

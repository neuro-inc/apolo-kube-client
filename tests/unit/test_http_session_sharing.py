from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from typing import Any
from unittest.mock import AsyncMock

import pytest
from aiohttp import ClientSession

from apolo_kube_client import KubeClient, KubeClientSelector, KubeConfig
from apolo_kube_client._errors import ResourceNotFound
from tests.unit.test_kube_client_selector import build_vcluster_secret


class _FakeResponse:
    async def json(self) -> dict[str, Any]:
        return {}


@pytest.mark.asyncio
async def test_plain_clients_share_http_session_but_use_distinct_ssl(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    session = ClientSession()
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

    client_a = KubeClient(config=cfg_a, http=session)
    client_b = KubeClient(config=cfg_b, http=session)

    try:
        async with client_a, client_b:
            await client_a._core.get(url="https://a")
            await client_b._core.get(url="https://b")
    finally:
        await session.close()

    # same session handled both requests
    assert len(captured_ssl) == 2
    # ensure different SSL contexts
    assert captured_ssl[0] is not captured_ssl[1]


@pytest.mark.asyncio
async def test_selector_uses_shared_session_and_distinct_ssl() -> None:
    session = ClientSession()

    # no SSL
    default = KubeClient(
        config=KubeConfig(endpoint_url="http://default.local"), http=session
    )

    selector = KubeClientSelector(default_client=default)

    secret = build_vcluster_secret(server="https://k1.local")
    default.core_v1.secret.get = AsyncMock(  # type: ignore[method-assign]
        side_effect=[ResourceNotFound(), secret]
    )

    try:
        async with selector:
            # default no SSL
            async with selector.get_client(org_name="o1", project_name="p1") as c1:
                assert c1._core._client is session
                assert c1._core._ssl_context is False

            # vcluster with SSL
            async with selector.get_client(org_name="o2", project_name="p2") as c2:
                assert c2._core._client is session
                assert c2._core._ssl_context is not False
    finally:
        await selector.aclose()
        await session.close()

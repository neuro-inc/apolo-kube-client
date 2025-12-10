import asyncio
import base64
from datetime import UTC, datetime
from unittest.mock import AsyncMock

import pytest
import yaml
from apolo_events_client import RecvEvent

from apolo_kube_client import KubeClientSelector, KubeConfig, V1ObjectMeta, V1Secret
from apolo_kube_client._errors import ResourceNotFound
from apolo_kube_client.apolo import generate_namespace_name


def build_vcluster_secret(server: str) -> V1Secret:
    ca_pem = "dummy-ca"
    cert_pem = "dummy-cert"
    key_pem = "dummy-key"
    config_payload = {
        "apiVersion": "v1",
        "clusters": [
            {
                "name": "vc",
                "cluster": {
                    "server": server,
                    "certificate-authority-data": base64.b64encode(
                        ca_pem.encode()
                    ).decode(),
                },
            }
        ],
        "contexts": [{"name": "vc", "context": {"cluster": "vc", "user": "vc"}}],
        "current-context": "vc",
        "users": [
            {
                "name": "vc",
                "user": {
                    "client-certificate-data": base64.b64encode(
                        cert_pem.encode()
                    ).decode(),
                    "client-key-data": base64.b64encode(key_pem.encode()).decode(),
                },
            }
        ],
    }
    config_data = base64.b64encode(yaml.safe_dump(config_payload).encode()).decode()
    secret_data = {
        "config": config_data,
        "client-certificate": base64.b64encode(cert_pem.encode()).decode(),
        "client-key": base64.b64encode(key_pem.encode()).decode(),
        "certificate-authority": base64.b64encode(ca_pem.encode()).decode(),
    }
    return V1Secret(metadata=V1ObjectMeta(name="vc-secret"), data=secret_data)


@pytest.fixture
def default_kube_config() -> KubeConfig:
    return KubeConfig(endpoint_url="http://localhost")


@pytest.fixture
def patch_secret_with_kubeconfig() -> str:
    return "kube"


async def test_returns_host_client_when_secret_missing(
    default_kube_config: KubeConfig,
    create_namespace_mock: AsyncMock,
) -> None:
    selector = KubeClientSelector(config=default_kube_config)
    selector._host_client.core_v1.secret.get = AsyncMock(  # type: ignore[method-assign]
        side_effect=ResourceNotFound()
    )
    async with selector:
        async with selector.get_client(org_name="org", project_name="proj") as client:
            assert client._origin is selector._host_client
            assert client._namespace == "platform--org--proj--405d80a888a4045e4dd515b6"


async def test_returns_vcluster_client_when_secret_present(
    default_kube_config: KubeConfig,
    patch_secret_with_kubeconfig: str,
) -> None:
    org = "org"
    project = "vc-project"

    # Patch secret for selector's default client and check
    secret = build_vcluster_secret(server=patch_secret_with_kubeconfig)
    selector = KubeClientSelector(config=default_kube_config)
    selector._host_client.core_v1.secret.get = AsyncMock(  # type: ignore[method-assign]
        return_value=secret
    )
    async with selector:
        async with selector.get_client(org_name=org, project_name=project) as client:
            assert client._namespace == "default"
            assert client.core_v1.secret._origin._get_ns(None) == "default"
            assert client.core_v1.secret._origin._get_ns("override") == "override"
    assert selector._host_client.core_v1.secret.get.await_count == 1


async def test_lru_eviction_closes_old_clients(
    default_kube_config: KubeConfig,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """
    vcluster_cache_size=1: first namespace is evicted when second is inserted (no active lease).
    Evicted client's __aexit__ and cleanup() should be called immediately.
    """
    secret_one = build_vcluster_secret(server="first")
    secret_two = build_vcluster_secret(server="second")
    selector = KubeClientSelector(config=default_kube_config, vcluster_cache_size=1)
    selector._host_client.core_v1.secret.get = AsyncMock(  # type: ignore[method-assign]
        side_effect=[secret_one, secret_two, secret_one]
    )

    closed_paths: list[str] = []

    def fake_rmtree(path: str, ignore_errors: bool = False) -> None:
        closed_paths.append(path)

    monkeypatch.setattr(
        "apolo_kube_client._vcluster._client_factory.shutil.rmtree", fake_rmtree
    )

    async with selector:
        async with selector.get_client(org_name="org", project_name="first"):
            pass

        assert not closed_paths

        async with selector.get_client(org_name="org", project_name="second"):
            pass

        assert len(closed_paths) == 1

        async with selector.get_client(org_name="org", project_name="first"):
            pass
        assert selector._host_client.core_v1.secret.get.await_count == 3


async def test_eviction_while_leased_uses_zombie_then_closes_on_release(
    default_kube_config: KubeConfig,
    patch_secret_with_kubeconfig: str,
) -> None:
    """
    Hold lease on first entry; inserting second causes eviction into 'zombie'.
    It must NOT close until we release the lease.
    """

    selector = KubeClientSelector(config=default_kube_config, vcluster_cache_size=1)
    secret = build_vcluster_secret(server=patch_secret_with_kubeconfig)
    selector._host_client.core_v1.secret.get = AsyncMock(  # type: ignore[method-assign]
        return_value=secret
    )

    async with selector:
        # Acquire namespace A and hold it while we create B
        ctx_entered = asyncio.Event()
        ctx_release = asyncio.Event()

        async def hold_a() -> None:
            async with selector.get_client(org_name="oA", project_name="pA") as c_a:
                assert c_a._origin is not selector._host_client
                assert str(c_a._origin._core.base_url) == patch_secret_with_kubeconfig
                ctx_entered.set()
                await ctx_release.wait()

        t = asyncio.create_task(hold_a())
        await ctx_entered.wait()

        # Now insert B while A is leased; A becomes zombie
        async with selector.get_client(org_name="oB", project_name="pB") as c_b:
            assert c_b._origin is not selector._host_client
            assert str(c_b._origin._core.base_url) == patch_secret_with_kubeconfig

        # should not be closed yet
        assert len(selector._vcluster_zombies) == 1
        assert list(selector._vcluster_zombies.values())[0].leases == 1

        # release. zombie should be cleaned up
        ctx_release.set()
        await t

        assert not selector._vcluster_zombies


async def test_concurrent_same_namespace_builds_once(
    default_kube_config: KubeConfig,
    patch_secret_with_kubeconfig: str,
) -> None:
    """
    Concurrent acquisitions for the same namespace
    must serialize to a single factory call.
    """
    selector = KubeClientSelector(config=default_kube_config, vcluster_cache_size=32)
    secret = build_vcluster_secret(server=patch_secret_with_kubeconfig)
    selector._host_client.core_v1.secret.get = AsyncMock(  # type: ignore[method-assign]
        return_value=secret
    )

    async with selector:

        async def worker() -> None:
            async with selector.get_client(org_name="o1", project_name="p1") as c:
                assert str(c._origin._core._base_url) == patch_secret_with_kubeconfig

        await asyncio.gather(*(worker() for _ in range(10)))

        # Only one build
        assert len(selector._vcluster_cache) == 1


async def test_aclose_waits_for_leases_then_closes(
    default_kube_config: KubeConfig,
    patch_secret_with_kubeconfig: str,
) -> None:
    """
    aclose waits for in-flight leases to end.
    """
    selector = KubeClientSelector(config=default_kube_config)
    secret = build_vcluster_secret(server=patch_secret_with_kubeconfig)
    selector._host_client.core_v1.secret.get = AsyncMock(  # type: ignore[method-assign]
        return_value=secret
    )

    async with selector:
        enter = asyncio.Event()
        release = asyncio.Event()

        async def user() -> None:
            async with selector.get_client(org_name="o1", project_name="p1"):
                enter.set()
                await release.wait()

        task = asyncio.create_task(user())
        await enter.wait()

        # Close in another task (will wait until release)
        closer = asyncio.create_task(selector.aclose())
        await asyncio.sleep(0)  # let aclose reach wait state
        assert not closer.done()

        # Release user and await close
        release.set()
        await task
        await closer

        assert not selector._vcluster_cache


async def test_vcluster_ready_event_pops_cache_entry(
    default_kube_config: KubeConfig,
) -> None:
    """
    _on_vcluster_ready must compute cache key and pop from cache.
    """
    selector = KubeClientSelector(config=default_kube_config)
    selector._vcluster_cache.pop = AsyncMock(return_value=None)  # type: ignore[method-assign]

    org = "org"
    project = "proj"
    ev = RecvEvent(
        tag="t1",
        timestamp=datetime.now(UTC),
        sender="test",
        stream="platform-vcluster",
        event_type="vcluster-ready",
        org=org,
        project=project,
    )

    await selector._on_vcluster_ready(ev)

    expected_key = generate_namespace_name(org, project)
    selector._vcluster_cache.pop.assert_awaited_once_with(expected_key)

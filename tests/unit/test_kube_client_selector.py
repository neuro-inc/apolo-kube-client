import asyncio
import base64
from collections.abc import Iterator
from unittest.mock import AsyncMock

import pytest
import yaml
from kubernetes.client.models import V1ObjectMeta, V1Secret

from apolo_kube_client import KubeClient, KubeClientSelector, KubeConfig
from apolo_kube_client._config import NAMESPACE_DEFAULT
from apolo_kube_client._errors import ResourceNotFound


@pytest.fixture
def default_kube_config() -> KubeConfig:
    return KubeConfig(endpoint_url="http://localhost", namespace=NAMESPACE_DEFAULT)


@pytest.fixture
def default_client(default_kube_config: KubeConfig) -> KubeClient:
    return KubeClient(config=default_kube_config)


@pytest.fixture
def patch_secret_with_kubeconfig(
    default_client: KubeClient,
) -> str:
    server_name = "kube"
    secret = _build_vcluster_secret(server=server_name)
    default_client.core_v1.secret.get = AsyncMock(return_value=secret)  # type: ignore[method-assign]
    return server_name


@pytest.fixture
def secret_raises_not_found(
    default_client: KubeClient,
) -> Iterator[None]:
    orig = default_client.core_v1.secret.get
    default_client.core_v1.secret.get = AsyncMock(side_effect=ResourceNotFound())  # type: ignore[method-assign]
    yield
    default_client.core_v1.secret.get = orig  # type: ignore[method-assign]


def _build_vcluster_secret(server: str) -> V1Secret:
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


async def test_returns_default_client_when_secret_missing(
    default_client: KubeClient,
    secret_raises_not_found: None,
) -> None:
    async with KubeClientSelector(default_client=default_client) as selector:
        async with selector.get_client(org_name="org", project_name="proj") as client:
            assert default_client is client
            assert client.core_v1.secret._get_ns("override") == "override"


async def test_returns_vcluster_client_when_secret_present(
    default_client: KubeClient,
    patch_secret_with_kubeconfig: str,
) -> None:
    selector = KubeClientSelector(default_client=default_client)

    org = "org"
    project = "vc-project"

    try:
        async with selector.get_client(org_name=org, project_name=project) as client:
            assert client.namespace == NAMESPACE_DEFAULT
            assert client.core_v1.secret._get_ns(None) == NAMESPACE_DEFAULT
            assert client.core_v1.secret._get_ns("override") == NAMESPACE_DEFAULT
    finally:
        await selector.aclose()
    assert default_client.core_v1.secret.get.await_count == 1  # type: ignore[attr-defined]


async def test_lru_eviction_closes_old_clients(
    default_client: KubeClient, monkeypatch: pytest.MonkeyPatch
) -> None:
    """
    vcluster_cache_size=1: first namespace is evicted when second is inserted (no active lease).
    Evicted client's __aexit__ and cleanup() should be called immediately.
    """
    secret_one = _build_vcluster_secret(server="first")
    secret_two = _build_vcluster_secret(server="second")
    default_client.core_v1.secret.get = AsyncMock(  # type: ignore[method-assign]
        side_effect=[secret_one, secret_two, secret_one]
    )

    closed_paths: list[str] = []

    def fake_rmtree(path: str, ignore_errors: bool = False) -> None:
        closed_paths.append(path)

    monkeypatch.setattr(
        "apolo_kube_client._vcluster._client_factory.shutil.rmtree", fake_rmtree
    )

    async with KubeClientSelector(
        default_client=default_client, vcluster_cache_size=1
    ) as selector:
        async with selector.get_client(org_name="org", project_name="first"):
            pass

        assert not closed_paths

        async with selector.get_client(org_name="org", project_name="second"):
            pass

        assert len(closed_paths) == 1

        async with selector.get_client(org_name="org", project_name="first"):
            pass
        assert default_client.core_v1.secret.get.await_count == 3


async def test_eviction_while_leased_uses_zombie_then_closes_on_release(
    default_client: KubeClient,
    patch_secret_with_kubeconfig: str,
) -> None:
    """
    Hold lease on first entry; inserting second causes eviction into 'zombie'.
    It must NOT close until we release the lease.
    """

    selector = KubeClientSelector(default_client=default_client, vcluster_cache_size=1)

    async with selector:
        # Acquire namespace A and hold it while we create B
        ctx_entered = asyncio.Event()
        ctx_release = asyncio.Event()

        async def hold_a() -> None:
            async with selector.get_client(org_name="oA", project_name="pA") as c_a:
                assert c_a is not default_client
                assert c_a.config.endpoint_url == patch_secret_with_kubeconfig
                ctx_entered.set()
                await ctx_release.wait()

        t = asyncio.create_task(hold_a())
        await ctx_entered.wait()

        # Now insert B while A is leased; A becomes zombie
        async with selector.get_client(org_name="oB", project_name="pB") as c_b:
            assert c_b is not default_client
            assert c_b.config.endpoint_url == patch_secret_with_kubeconfig

        # should not be closed yet
        assert len(selector._vcluster_zombies) == 1
        assert list(selector._vcluster_zombies.values())[0].leases == 1

        # release. zombie should be cleaned up
        ctx_release.set()
        await t

        assert not selector._vcluster_zombies


async def test_concurrent_same_namespace_builds_once(
    default_client: KubeClient,
    patch_secret_with_kubeconfig: str,
) -> None:
    """
    Concurrent acquisitions for the same namespace
    must serialize to a single factory call.
    """
    selector = KubeClientSelector(default_client=default_client, vcluster_cache_size=32)

    async with selector:

        async def worker() -> None:
            async with selector.get_client(org_name="o1", project_name="p1") as c:
                assert c.config.endpoint_url == patch_secret_with_kubeconfig

        await asyncio.gather(*(worker() for _ in range(10)))

        # Only one build
        assert len(selector._vcluster_cache) == 1


async def test_aclose_waits_for_leases_then_closes(
    default_client: KubeClient,
    patch_secret_with_kubeconfig: str,
) -> None:
    """
    aclose waits for in-flight leases to end.
    """
    selector = KubeClientSelector(default_client=default_client)

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

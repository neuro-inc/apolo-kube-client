from collections.abc import AsyncGenerator, Callable
from uuid import uuid4

import pytest

from apolo_kube_client import KubeClient, V1ConfigMap, V1ObjectMeta


@pytest.fixture
def config_map_model_factory() -> Callable[[str, dict[str, str] | None], V1ConfigMap]:
    def _create_config_map(
        name: str, data: dict[str, str] | None = None
    ) -> V1ConfigMap:
        data = data or {}
        return V1ConfigMap(
            metadata=V1ObjectMeta(name=name, namespace="default"),
            data=data,
        )

    return _create_config_map


@pytest.fixture
async def config_map(
    kube_client: KubeClient,
    config_map_model_factory: Callable[[str, dict[str, str] | None], V1ConfigMap],
) -> AsyncGenerator[V1ConfigMap]:
    config_map = config_map_model_factory(
        f"test-configmap-{uuid4().hex[:8]}",
        {
            "key1": "value1",
            "key2": "value2",
        },
    )
    created = await kube_client.core_v1.config_map.create(
        model=config_map, namespace="default"
    )
    assert created.metadata.name
    yield created
    await kube_client.core_v1.config_map.delete(
        name=created.metadata.name,
        namespace="default",
    )


class TestConfigMap:
    async def test_crud(
        self,
        config_map_model_factory: Callable[[str, dict[str, str] | None], V1ConfigMap],
        kube_client: KubeClient,
    ) -> None:
        config_map = config_map_model_factory(
            "configmap",
            {"username": "user", "password": "pw"},
        )
        assert config_map.metadata.name

        # create
        created = await kube_client.core_v1.config_map.create(
            model=config_map, namespace="default"
        )
        assert created.metadata.name == config_map.metadata.name
        assert created.data == config_map.data

        # get
        fetched = await kube_client.core_v1.config_map.get(
            name=config_map.metadata.name
        )
        assert fetched.data == config_map.data

        # list
        config_maps = await kube_client.core_v1.config_map.get_list()
        names = {cm.metadata.name for cm in config_maps.items}
        assert config_map.metadata.name in names

        # delete
        await kube_client.core_v1.config_map.delete(name=config_map.metadata.name)

    async def test_add_remove_keys(
        self,
        config_map: V1ConfigMap,
        kube_client: KubeClient,
    ) -> None:
        assert config_map.metadata.name

        updated = await kube_client.core_v1.config_map.add_key(
            name=config_map.metadata.name,
            key="password",
            value="password",
            namespace="default",
        )
        assert updated.data["password"] == "password"

        without_password = await kube_client.core_v1.config_map.delete_key(
            name=config_map.metadata.name,
            key="password",
            namespace="default",
        )
        assert without_password.data.get("password") is None

    async def test_add_remove_add_keys(
        self,
        config_map: V1ConfigMap,
        kube_client: KubeClient,
    ) -> None:
        assert config_map.metadata.name

        await kube_client.core_v1.config_map.add_key(
            name=config_map.metadata.name,
            key="feature",
            value="on",
            namespace="default",
        )
        await kube_client.core_v1.config_map.delete_key(
            name=config_map.metadata.name,
            key="feature",
            namespace="default",
        )

        updated = await kube_client.core_v1.config_map.add_key(
            name=config_map.metadata.name,
            key="feature",
            value="off",
            namespace="default",
        )
        assert updated.data["feature"] == "off"

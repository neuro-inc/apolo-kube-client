from collections.abc import AsyncGenerator, Callable
from uuid import uuid4

import pytest
from kubernetes.client.models import V1Namespace, V1ObjectMeta

from apolo_kube_client import KubeClient
from apolo_kube_client._errors import ResourceExists, ResourceNotFound


@pytest.fixture
def namespace_model_factory() -> Callable[[str, dict[str, str] | None], V1Namespace]:
    def _create_namespace_model(
        name: str, labels: dict[str, str] | None = None
    ) -> V1Namespace:
        labels = labels or {}
        return V1Namespace(
            api_version="v1",
            kind="Namespace",
            metadata=V1ObjectMeta(name=name, labels=labels),
        )

    return _create_namespace_model


@pytest.fixture
async def namespace(
    kube_client: KubeClient,
    namespace_model_factory: Callable[[str, dict[str, str] | None], V1Namespace],
) -> AsyncGenerator[V1Namespace]:
    namespace = namespace_model_factory(f"test-ns-{uuid4().hex[:8]}", None)
    yield await kube_client.core_v1.namespace.create(model=namespace)
    await kube_client.core_v1.namespace.delete(name=namespace.metadata.name)


class TestNamespace:
    async def test_crud(
        self,
        kube_client: KubeClient,
        namespace_model_factory: Callable[[str, dict[str, str] | None], V1Namespace],
    ) -> None:
        namespace = namespace_model_factory("test-ns", None)

        # create namespace and ensure it was created
        namespace_create = await kube_client.core_v1.namespace.create(model=namespace)
        assert namespace_create.metadata.name == namespace.metadata.name

        # let's get the namespace and ensure it exists
        namespace_get = await kube_client.core_v1.namespace.get(
            name=namespace.metadata.name
        )
        assert namespace_get.metadata.name == namespace.metadata.name

        # let's get all namespaces and ensure that newly created namespace is there
        namespace_list = await kube_client.core_v1.namespace.get_list()
        namespace_names = {n.metadata.name for n in namespace_list.items}
        assert len(namespace_list.items) > 0
        assert namespace.metadata.name in namespace_names

        # delete and ensure phase changed
        namespace_delete = await kube_client.core_v1.namespace.delete(
            name=namespace.metadata.name
        )
        assert namespace_delete.status.phase == "Terminating"

    async def test_get_or_create(
        self,
        kube_client: KubeClient,
        namespace_model_factory: Callable[[str, dict[str, str] | None], V1Namespace],
        namespace: V1Namespace,
    ) -> None:
        # Test getting an existing namespace
        (
            created,
            namespace_get_or_create,
        ) = await kube_client.core_v1.namespace.get_or_create(model=namespace)
        assert namespace_get_or_create.metadata.name == namespace.metadata.name
        assert created is False

        # Test creating a new namespace
        namespace = namespace_model_factory("test-get-or-create-ns-new", None)
        (
            created,
            namespace_get_or_create,
        ) = await kube_client.core_v1.namespace.create_or_update(model=namespace)
        assert namespace_get_or_create.metadata.name == "test-get-or-create-ns-new"
        assert created is True
        # Clean up the created namespace
        await kube_client.core_v1.namespace.delete(name=namespace.metadata.name)

    async def test_create_or_update(
        self,
        kube_client: KubeClient,
        namespace_model_factory: Callable[[str, dict[str, str] | None], V1Namespace],
        namespace: V1Namespace,
    ) -> None:
        # Test updating an existing namespace
        namespace.metadata.labels = {"new_label": "some_value"}
        (
            created,
            namespace_create_or_update,
        ) = await kube_client.core_v1.namespace.create_or_update(model=namespace)
        assert namespace_create_or_update.metadata.name == namespace.metadata.name
        assert namespace.metadata.labels["new_label"] == "some_value"
        assert created is False

        # Test creating a new namespace
        namespace = namespace_model_factory("test-create-or-updated-ns-new", None)
        (
            created,
            namespace_create_or_update,
        ) = await kube_client.core_v1.namespace.create_or_update(model=namespace)
        assert created is True
        assert (
            namespace_create_or_update.metadata.name == "test-create-or-updated-ns-new"
        )
        # Clean up the created namespace
        await kube_client.core_v1.namespace.delete(name=namespace.metadata.name)

    async def test_patch_json(
        self, kube_client: KubeClient, namespace: V1Namespace
    ) -> None:
        patch_json_list = [
            {
                "op": "add",
                "path": f"/metadata/labels/{kube_client.escape_json_pointer('platform.apolo.us/app')}",
                "value": "my-app",
            }
        ]
        namespace = await kube_client.core_v1.namespace.patch_json(
            name=namespace.metadata.name, patch_json_list=patch_json_list
        )
        assert namespace.metadata.labels["platform.apolo.us/app"] == "my-app"

    async def test_exception(
        self, kube_client: KubeClient, namespace: V1Namespace
    ) -> None:
        with pytest.raises(ResourceNotFound):
            await kube_client.core_v1.namespace.get(name="non-existing-namespace")

        with pytest.raises(ResourceExists):
            namespace = V1Namespace(metadata=V1ObjectMeta(name=namespace.metadata.name))
            await kube_client.core_v1.namespace.create(model=namespace)

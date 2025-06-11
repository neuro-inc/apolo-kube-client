from collections.abc import AsyncGenerator
from uuid import uuid4

import pytest
from kubernetes.client.models import V1Namespace, V1ObjectMeta

from apolo_kube_client import KubeClient
from apolo_kube_client._errors import ResourceExists, ResourceNotFound


@pytest.fixture
async def namespace(
    kube_client: KubeClient, request: pytest.FixtureRequest
) -> AsyncGenerator[V1Namespace]:
    name = getattr(request, "param", f"test-ns-{uuid4().hex[:8]}")
    namespace = V1Namespace(metadata=V1ObjectMeta(name=name))
    yield await kube_client.core_v1.namespace.create(model=namespace)
    await kube_client.core_v1.namespace.delete(name=name)


class TestNamespace:
    async def test_crud(self, kube_client: KubeClient) -> None:
        namespace = V1Namespace(
            api_version="v1", kind="Namespace", metadata=V1ObjectMeta(name="test-ns")
        )

        # create namespace and ensure it was created
        namespace_create = await kube_client.core_v1.namespace.create(model=namespace)
        assert namespace_create.metadata.name == namespace.metadata.name

        # let's get the namespace and ensure it exists
        namespace_get = await kube_client.core_v1.namespace.get(
            name=namespace.metadata.name
        )
        assert namespace_get.metadata.name == namespace.metadata.name

        # let's get all namespaces and ensure that newly created namespace is there
        namespace_list = await kube_client.core_v1.namespace.list()
        namespace_names = {n.metadata.name for n in namespace_list.items}
        assert len(namespace_list.items) > 0
        assert namespace.metadata.name in namespace_names

        # delete and ensure phase changed
        namespace_delete = await kube_client.core_v1.namespace.delete(
            name=namespace.metadata.name
        )
        assert namespace_delete.status.phase == "Terminating"

    async def test_exception(
        self, kube_client: KubeClient, namespace: V1Namespace
    ) -> None:
        with pytest.raises(ResourceNotFound):
            await kube_client.core_v1.namespace.get(name="non-existing-namespace")

        with pytest.raises(ResourceExists):
            namespace = V1Namespace(metadata=V1ObjectMeta(name=namespace.metadata.name))
            await kube_client.core_v1.namespace.create(model=namespace)

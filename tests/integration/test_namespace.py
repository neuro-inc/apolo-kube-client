from uuid import uuid4

import pytest

from apolo_kube_client.client import KubeClient
from apolo_kube_client.namespace import NamespaceApi


class TestNamespaceApi:
    @pytest.fixture
    async def namespace_api(self, kube_client: KubeClient) -> NamespaceApi:
        return NamespaceApi(kube_client)

    async def test__get_all_namespaces(
        self,
        namespace_api: NamespaceApi,
    ) -> None:
        namespaces = await namespace_api.get_namespaces()
        assert len(namespaces) > 0

    async def test__get_namespace(
        self,
        namespace_api: NamespaceApi,
    ) -> None:
        namespace = await namespace_api.get_namespace("default")
        assert namespace.name == "default"

    async def test__create_namespace(
        self,
        namespace_api: NamespaceApi,
    ) -> None:
        name = uuid4().hex
        created_namespace = await namespace_api.create_namespace(name)

        assert created_namespace.name == name

        # let's get all namespaces and ensure that newly created namespace is there
        namespaces = await namespace_api.get_namespaces()
        namespaces_by_name = {n.name: n for n in namespaces}
        assert name in namespaces_by_name

        # let's also get a namespace by the name
        namespace = await namespace_api.get_namespace(name)
        assert namespace.uid == created_namespace.uid
        assert namespace.name == created_namespace.name

        # delete and ensure phase changed
        response = await namespace_api.delete_namespace(name)
        assert response["status"]["phase"] == "Terminating"

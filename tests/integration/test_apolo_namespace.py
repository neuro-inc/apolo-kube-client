import pytest

from apolo_kube_client.apolo import (
    NAMESPACE_ORG_LABEL,
    NAMESPACE_PROJECT_LABEL,
    create_namespace,
    generate_hash,
    normalize_name,
)
from apolo_kube_client.client import KubeClient
from apolo_kube_client.namespace import NamespaceApi


class TestApoloNamespace:
    @pytest.fixture
    def org_name(self) -> str:
        return "org"

    @pytest.fixture
    def project_name(self) -> str:
        return "project"

    async def test__create_apolo_namespace(
        self,
        org_name: str,
        project_name: str,
        kube_client: KubeClient,
    ) -> None:
        namespace = await create_namespace(
            kube_client,
            org_name,
            project_name,
        )

        # ensure a name was properly generated
        org_project_hash = generate_hash(f"{org_name}--{project_name}")
        assert namespace.name == f"platform--org--project--{org_project_hash}"

        # ensure labels were set
        assert namespace.labels_as_dict[NAMESPACE_ORG_LABEL] == org_name
        assert namespace.labels_as_dict[NAMESPACE_PROJECT_LABEL] == project_name

        # ensure a NetworkPolicy for this namespace were created
        network_policies = await kube_client.get(
            kube_client.generate_network_policy_url(namespace.name)
        )
        assert len(network_policies["items"]) == 1
        actual_network_policy = network_policies["items"][0]
        metadata = actual_network_policy["metadata"]
        spec = actual_network_policy["spec"]
        assert metadata["name"] == namespace.name
        assert metadata["namespace"] == namespace.name

        assert spec["policyTypes"] == ["Ingress", "Egress"]
        assert spec["podSelector"] == {}
        assert spec["ingress"][0]["from"][0]["podSelector"] == {}
        assert spec["egress"][0]["to"][0]["podSelector"] == {}

        assert spec["ingress"][0]["from"][0]["namespaceSelector"] == {
            "matchLabels": {"namespace": namespace.name}
        }
        assert spec["egress"][0]["to"][0]["namespaceSelector"] == {
            "matchLabels": {"namespace": namespace.name}
        }

        # delete and ensure phase changed
        namespace_api = NamespaceApi(kube_client)
        response = await namespace_api.delete_namespace(namespace.name)
        assert response["status"]["phase"] == "Terminating"

    async def test__create_apolo_namespace__project_with_slashes(
        self,
        org_name: str,
        kube_client: KubeClient,
    ) -> None:
        project_name = "some/project/name"
        normalized_project_name = normalize_name(project_name)

        namespace = await create_namespace(
            kube_client,
            org_name,
            project_name,
        )

        # ensure a name was properly generated
        org_project_hash = generate_hash(f"{org_name}--{normalized_project_name}")
        assert namespace.name == f"platform--org--some-project-name--{org_project_hash}"

        # ensure labels were set
        assert namespace.labels_as_dict[NAMESPACE_ORG_LABEL] == org_name
        assert (
            namespace.labels_as_dict[NAMESPACE_PROJECT_LABEL] == normalized_project_name
        )

        # delete and ensure phase changed
        namespace_api = NamespaceApi(kube_client)
        response = await namespace_api.delete_namespace(namespace.name)
        assert response["status"]["phase"] == "Terminating"

    # todo: test network policies

import pytest

from apolo_kube_client import KubeClient
from apolo_kube_client.apolo import (
    COMPONENT_LABEL,
    NAMESPACE_ORG_LABEL,
    NAMESPACE_PROJECT_LABEL,
    create_namespace,
    generate_hash,
    normalize_name,
)
from apolo_kube_client import (
    V1IPBlock,
    V1LabelSelector,
    V1NetworkPolicyEgressRule,
    V1NetworkPolicyPeer,
    V1NetworkPolicyPort,
)


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
        assert (
            namespace.metadata.name
            == f"platform--{org_name}--{project_name}--{org_project_hash}"
        )

        # ensure labels were set
        assert namespace.metadata.labels[NAMESPACE_ORG_LABEL] == org_name
        assert namespace.metadata.labels[NAMESPACE_PROJECT_LABEL] == project_name

        # ensure a NetworkPolicy for this namespace were created
        np = await kube_client.networking_k8s_io_v1.network_policy.get(
            name=namespace.metadata.name, namespace=namespace.metadata.name
        )
        assert np.metadata.name == namespace.metadata.name
        assert np.metadata.namespace == namespace.metadata.name

        assert np.spec.policy_types == ["Egress"]
        assert np.spec.egress[-1].to[0].ip_block is not None

        assert np.spec.egress == [
            V1NetworkPolicyEgressRule(
                to=[
                    V1NetworkPolicyPeer(
                        namespace_selector=V1LabelSelector(
                            match_labels={
                                NAMESPACE_ORG_LABEL: org_name,
                                NAMESPACE_PROJECT_LABEL: project_name,
                            }
                        ),
                        pod_selector=V1LabelSelector(),
                    )
                ]
            ),
            V1NetworkPolicyEgressRule(
                to=[
                    V1NetworkPolicyPeer(
                        ip_block=V1IPBlock(
                            cidr="0.0.0.0/0",
                            except_=[
                                "10.0.0.0/8",
                                "172.16.0.0/12",
                                "192.168.0.0/16",
                            ],
                        )
                    )
                ]
            ),
            V1NetworkPolicyEgressRule(
                to=[
                    V1NetworkPolicyPeer(ip_block=V1IPBlock(cidr="10.0.0.0/8")),
                    V1NetworkPolicyPeer(ip_block=V1IPBlock(cidr="172.16.0.0/12")),
                    V1NetworkPolicyPeer(ip_block=V1IPBlock(cidr="192.168.0.0/16")),
                ],
                ports=[
                    V1NetworkPolicyPort(port=53, protocol="UDP"),
                    V1NetworkPolicyPort(port=53, protocol="TCP"),
                ],
            ),
            V1NetworkPolicyEgressRule(
                to=[
                    V1NetworkPolicyPeer(
                        namespace_selector=V1LabelSelector(),
                        pod_selector=V1LabelSelector(
                            match_labels={COMPONENT_LABEL: "ingress-gateway"}
                        ),
                    )
                ],
            ),
            V1NetworkPolicyEgressRule(
                to=[
                    V1NetworkPolicyPeer(
                        ip_block=V1IPBlock(cidr=np.spec.egress[-1].to[0].ip_block.cidr)
                    )
                ],
                ports=[
                    V1NetworkPolicyPort(
                        port=np.spec.egress[-1].ports[0].port, protocol="TCP"
                    )
                ],
            ),
        ]

        # delete and ensure phase changed
        namespace_delete = await kube_client.core_v1.namespace.delete(
            name=namespace.metadata.name
        )
        assert namespace_delete.status.phase == "Terminating"

    async def test__already_created_apolo_namespace(
        self,
        org_name: str,
        kube_client: KubeClient,
    ) -> None:
        project_name = "proj-already-created"
        await create_namespace(
            kube_client,
            org_name,
            project_name,
        )
        # namespace was already created and should not raise when called again
        namespace = await create_namespace(
            kube_client,
            org_name,
            project_name,
        )

        # ensure a name was properly generated
        org_project_hash = generate_hash(f"{org_name}--{project_name}")
        assert (
            namespace.metadata.name
            == f"platform--{org_name}--{project_name}--{org_project_hash}"
        )

        # ensure labels were set
        assert namespace.metadata.labels[NAMESPACE_ORG_LABEL] == org_name
        assert namespace.metadata.labels[NAMESPACE_PROJECT_LABEL] == project_name

        # ensure a NetworkPolicy for this namespace were created
        await kube_client.networking_k8s_io_v1.network_policy.get(
            name=namespace.metadata.name, namespace=namespace.metadata.name
        )

        # delete and ensure phase changed
        namespace_delete = await kube_client.core_v1.namespace.delete(
            name=namespace.metadata.name
        )
        assert namespace_delete.status.phase == "Terminating"

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
        assert (
            namespace.metadata.name
            == f"platform--org--some-project-name--{org_project_hash}"
        )

        # ensure labels were set
        assert namespace.metadata.labels[NAMESPACE_ORG_LABEL] == org_name
        assert (
            namespace.metadata.labels[NAMESPACE_PROJECT_LABEL]
            == normalized_project_name
        )

        # delete and ensure phase changed
        namespace_delete = await kube_client.core_v1.namespace.delete(
            name=namespace.metadata.name
        )
        assert namespace_delete.status.phase == "Terminating"


# todo: test network policies

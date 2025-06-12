from kubernetes.client.models import (
    V1LabelSelector,
    V1NetworkPolicy,
    V1NetworkPolicyEgressRule,
    V1NetworkPolicyIngressRule,
    V1NetworkPolicyPeer,
    V1NetworkPolicySpec,
    V1ObjectMeta,
)

from apolo_kube_client import KubeClient


class TestNetworkPolicy:
    async def test_crud(self, kube_client: KubeClient) -> None:
        np = V1NetworkPolicy(
            api_version="networking.k8s.io/v1",
            kind="NetworkPolicy",
            metadata=V1ObjectMeta(name="allow-all-ingress"),
            spec=V1NetworkPolicySpec(
                pod_selector=V1LabelSelector(match_labels={}),
                ingress=[
                    V1NetworkPolicyIngressRule(
                        _from=[
                            V1NetworkPolicyPeer(
                                pod_selector=V1LabelSelector(match_labels={})
                            )
                        ],
                    )
                ],
                egress=[
                    V1NetworkPolicyEgressRule(
                        to=[
                            V1NetworkPolicyPeer(
                                pod_selector=V1LabelSelector(match_labels={})
                            )
                        ],
                    )
                ],
                policy_types=["Ingress", "Egress"],
            ),
        )

        # test creating a network policy
        np_create = await kube_client.networking_k8s_io_v1.network_policy.create(
            model=np, namespace="default"
        )
        assert np_create.metadata.name == np.metadata.name

        # test getting the network policy
        np_get = await kube_client.networking_k8s_io_v1.network_policy.get(
            name=np.metadata.name
        )
        assert np_get.metadata.name == np.metadata.name

        # test listing network policies
        np_list = await kube_client.networking_k8s_io_v1.network_policy.list()
        np_names = {n.metadata.name for n in np_list.items}
        assert len(np_list.items) > 0
        assert np.metadata.name in np_names

        # test deleting the network policy
        np_status = await kube_client.networking_k8s_io_v1.network_policy.delete(
            name=np.metadata.name
        )
        assert np_status.status == "Success"

    # TODO: add tests with check connectivity between pods

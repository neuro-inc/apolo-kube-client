from kubernetes.client.models import V1NetworkPolicy, V1NetworkPolicyList, V1Status

from .._networking_k8s_io_v1 import NetworkingK8SioV1Api, NetworkPolicy
from ._attr import attr
from ._base_resource import Base, ProjectResource


class PrNetworkPolicy(
    ProjectResource[V1NetworkPolicy, V1NetworkPolicyList, V1Status, NetworkPolicy]
):
    pass


class PrNetworkingK8SioV1Api(Base[NetworkingK8SioV1Api]):
    """
    NetworkK8sIo v1 API wrapper for Kubernetes.
    """

    @attr(PrNetworkPolicy)
    def network_policy(self) -> NetworkPolicy:
        return self._origin.network_policy

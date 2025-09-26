from kubernetes.client.models import V1NetworkPolicy, V1NetworkPolicyList, V1Status

from .._networking_k8s_io_v1 import NetworkingK8SioV1Api, NetworkPolicy
from ._attr_proxy import attr
from ._resource_proxy import BaseProxy, NamespacedResourceProxy


class NetworkPolicyProxy(
    NamespacedResourceProxy[
        V1NetworkPolicy, V1NetworkPolicyList, V1Status, NetworkPolicy
    ]
):
    pass


class NetworkingK8SioV1ApiProxy(BaseProxy[NetworkingK8SioV1Api]):
    """
    NetworkK8sIo v1 API wrapper for Kubernetes.
    """

    @attr(NetworkPolicyProxy)
    def network_policy(self) -> NetworkPolicy:
        return self._origin.network_policy

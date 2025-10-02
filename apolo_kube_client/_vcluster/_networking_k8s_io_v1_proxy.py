from kubernetes.client.models import (
    V1Ingress,
    V1IngressList,
    V1NetworkPolicy,
    V1NetworkPolicyList,
    V1Status,
)

from .._networking_k8s_io_v1 import Ingress, NetworkingK8SioV1Api, NetworkPolicy
from ._attr_proxy import attr
from ._resource_proxy import BaseProxy, NamespacedResourceProxy


class NetworkPolicyProxy(
    NamespacedResourceProxy[
        V1NetworkPolicy, V1NetworkPolicyList, V1Status, NetworkPolicy
    ]
):
    pass


class IngressProxy(
    NamespacedResourceProxy[V1Ingress, V1IngressList, V1Status, Ingress]
):
    pass


class NetworkingK8SioV1ApiProxy(BaseProxy[NetworkingK8SioV1Api]):
    """
    NetworkK8sIo v1 API wrapper for Kubernetes.
    """

    @attr(NetworkPolicyProxy)
    def network_policy(self) -> NetworkPolicy:
        return self._origin.network_policy

    @attr(IngressProxy)
    def ingress(self) -> Ingress:
        return self._origin.ingress

from kubernetes.client.models import V1NetworkPolicy, V1NetworkPolicyList, V1Status

from ._attr import _Attr
from ._base_resource import Base, NamespacedResource


class NetworkPolicy(NamespacedResource[V1NetworkPolicy, V1NetworkPolicyList, V1Status]):
    query_path = "networkpolicies"


class NetworkingK8SioV1Api(Base):
    """
    NetworkK8sIo v1 API wrapper for Kubernetes.
    """

    group_api_query_path = "apis/networking.k8s.io/v1"
    network_policy = _Attr(NetworkPolicy, group_api_query_path)

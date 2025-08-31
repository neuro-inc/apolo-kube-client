from kubernetes.client.models import V1NetworkPolicy, V1NetworkPolicyList, V1Status

from ._base_resource import NamespacedResource
from ._core import _KubeCore


class NetworkingK8SioV1Api:
    """
    NetworkK8sIo v1 API wrapper for Kubernetes.
    """

    group_api_query_path = "apis/networking.k8s.io/v1"

    def __init__(self, core: _KubeCore) -> None:
        self._core = core
        self.network_policy = NetworkPolicy(core, self.group_api_query_path)


class NetworkPolicy(NamespacedResource[V1NetworkPolicy, V1NetworkPolicyList, V1Status]):
    query_path = "networkpolicies"

from kubernetes.client import ApiClient
from kubernetes.client.models import (
    V1EndpointSlice,
    V1EndpointSliceList,
)

from apolo_kube_client._base_resource import NamespacedResource
from apolo_kube_client._core import _KubeCore


class DiscoveryK8sIoV1Api:
    """
    discovery.k8s.io/v1 API wrapper for Kubernetes.
    """

    group_api_query_path = "apis/discovery.k8s.io/v1"

    def __init__(self, core: _KubeCore, api_client: ApiClient) -> None:
        self._core = core
        self.endpoint_slice = EndpointSlice(core, self.group_api_query_path, api_client)


class EndpointSlice(
    NamespacedResource[V1EndpointSlice, V1EndpointSliceList, V1EndpointSlice]
):
    query_path = "endpointslices"

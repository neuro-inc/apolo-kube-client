from kubernetes.client.models import (
    V1EndpointSlice,
    V1EndpointSliceList,
)

from ._base_resource import NamespacedResource
from ._core import _KubeCore


class DiscoveryK8sIoV1Api:
    """
    discovery.k8s.io/v1 API wrapper for Kubernetes.
    """

    group_api_query_path = "apis/discovery.k8s.io/v1"

    def __init__(self, core: _KubeCore) -> None:
        self._core = core
        self.endpoint_slice = EndpointSlice(core, self.group_api_query_path)


class EndpointSlice(
    NamespacedResource[V1EndpointSlice, V1EndpointSliceList, V1EndpointSlice]
):
    query_path = "endpointslices"

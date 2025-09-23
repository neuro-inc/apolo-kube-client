from kubernetes.client.models import (
    V1EndpointSlice,
    V1EndpointSliceList,
)

from ._attr import _Attr
from ._base_resource import NamespacedResource
from ._core import _KubeCore


class EndpointSlice(
    NamespacedResource[V1EndpointSlice, V1EndpointSliceList, V1EndpointSlice]
):
    query_path = "endpointslices"


class DiscoveryK8sIoV1Api:
    """
    discovery.k8s.io/v1 API wrapper for Kubernetes.
    """

    group_api_query_path = "apis/discovery.k8s.io/v1"
    endpoint_slice = _Attr(EndpointSlice, group_api_query_path)

    def __init__(self, core: _KubeCore) -> None:
        self._core = core

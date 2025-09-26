from kubernetes.client.models import (
    V1EndpointSlice,
    V1EndpointSliceList,
)

from .._discovery_k8s_io_v1 import DiscoveryK8sIoV1Api, EndpointSlice
from ._virt_attr import attr
from ._virt_base_resource import Base, VirtualResource


class VirtEndpointSlice(
    VirtualResource[
        V1EndpointSlice, V1EndpointSliceList, V1EndpointSlice, EndpointSlice
    ]
):
    pass


class VirtDiscoveryK8sIoV1Api(Base[DiscoveryK8sIoV1Api]):
    """
    discovery.k8s.io/v1 API wrapper for Kubernetes.
    """

    @attr(VirtEndpointSlice)
    def endpoint_slice(self) -> EndpointSlice:
        return self._origin.endpoint_slice

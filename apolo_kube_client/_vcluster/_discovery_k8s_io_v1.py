from kubernetes.client.models import (
    V1EndpointSlice,
    V1EndpointSliceList,
)

from .._discovery_k8s_io_v1 import DiscoveryK8sIoV1Api, EndpointSlice
from ._attr import attr
from ._base_resource import Base, ProjectResource


class PrEndpointSlice(
    ProjectResource[
        V1EndpointSlice, V1EndpointSliceList, V1EndpointSlice, EndpointSlice
    ]
):
    pass


class PrDiscoveryK8sIoV1Api(Base[DiscoveryK8sIoV1Api]):
    """
    discovery.k8s.io/v1 API wrapper for Kubernetes.
    """

    @attr(PrEndpointSlice)
    def endpoint_slice(self) -> EndpointSlice:
        return self._origin.endpoint_slice

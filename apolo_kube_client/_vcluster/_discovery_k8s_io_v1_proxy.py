from kubernetes.client.models import (
    V1EndpointSlice,
    V1EndpointSliceList,
)

from .._discovery_k8s_io_v1 import DiscoveryK8sIoV1Api, EndpointSlice
from ._attr_proxy import attr
from ._resource_proxy import BaseProxy, NamespacedResourceProxy


class EndpointSliceProxy(
    NamespacedResourceProxy[
        V1EndpointSlice, V1EndpointSliceList, V1EndpointSlice, EndpointSlice
    ]
):
    pass


class DiscoveryK8sIoV1ApiProxy(BaseProxy[DiscoveryK8sIoV1Api]):
    """
    discovery.k8s.io/v1 API wrapper for Kubernetes.
    """

    @attr(EndpointSliceProxy)
    def endpoint_slice(self) -> EndpointSlice:
        return self._origin.endpoint_slice

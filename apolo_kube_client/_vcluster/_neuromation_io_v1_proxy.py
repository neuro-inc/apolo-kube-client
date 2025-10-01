from kubernetes.client.models import V1Status

from .._crd_models import V1DiskNamingCRD, V1DiskNamingCRDList
from .._neuromation_io_v1 import DiskNamingCRD, NeuromationioV1API
from ._attr_proxy import attr
from ._resource_proxy import BaseProxy, NamespacedResourceProxy


class DiskNamingCRDProxy(
    NamespacedResourceProxy[
        V1DiskNamingCRD, V1DiskNamingCRDList, V1Status, DiskNamingCRD  # type: ignore
    ]
):
    pass


class NeuromationioV1APIProxy(BaseProxy[NeuromationioV1API]):
    """
    Neuromation.io v1 API wrapper for Kubernetes.
    """

    @attr(DiskNamingCRDProxy)
    def disk_naming(self) -> DiskNamingCRD:
        return self._origin.disk_naming

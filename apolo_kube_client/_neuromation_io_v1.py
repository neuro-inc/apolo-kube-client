from kubernetes.client.models import V1Status

from ._attr import _Attr
from ._base_resource import Base, NamespacedResource
from ._crd_models import V1DiskNamingCRD, V1DiskNamingCRDList


class DiskNamingCRD(NamespacedResource[V1DiskNamingCRD, V1DiskNamingCRDList, V1Status]):  # type: ignore
    query_path = "disknamings"


class NeuromationioV1API(Base):
    """
    Neuromation.io v1 API wrapper for Kubernetes.
    """

    group_api_query_path = "apis/neuromation.io/v1"
    disk_naming = _Attr(DiskNamingCRD, group_api_query_path)

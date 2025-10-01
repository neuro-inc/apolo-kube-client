from kubernetes.client.models import V1StorageClass, V1StorageClassList

from ._attr import _Attr
from ._base_resource import Base, ClusterScopedResource


class StorageClass(
    ClusterScopedResource[V1StorageClass, V1StorageClassList, V1StorageClass]
):
    query_path = "storageclasses"


class StorageK8SioV1Api(Base):
    """
    StorageK8Sio v1 API wrapper for Kubernetes.
    """

    group_api_query_path = "apis/storage.k8s.io/v1"
    storage_class = _Attr(StorageClass, group_api_query_path)

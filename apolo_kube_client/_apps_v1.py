from kubernetes.client.models import V1StatefulSet, V1StatefulSetList, V1Status

from ._attr import _Attr
from ._base_resource import Base, NamespacedResource


class StatefulSet(NamespacedResource[V1StatefulSet, V1StatefulSetList, V1Status]):
    query_path = "statefulsets"


class AppsV1Api(Base):
    """
    Apps v1 API wrapper for Kubernetes.
    """

    group_api_query_path = "apis/apps/v1"

    statefulset = _Attr(StatefulSet, group_api_query_path)

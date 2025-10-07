from kubernetes.client.models import (
    V1StatefulSet,
    V1StatefulSetList,
    V1Status,
)

from .._apps_v1 import AppsV1Api, StatefulSet
from ._attr_proxy import attr
from ._resource_proxy import BaseProxy, NamespacedResourceProxy


class StatefulSetProxy(
    NamespacedResourceProxy[V1StatefulSet, V1StatefulSetList, V1Status, StatefulSet]
):
    pass


class AppsV1ApiProxy(BaseProxy[AppsV1Api]):
    """
    Apps v1 API Proxy wrapper for Kubernetes.
    """

    @attr(StatefulSetProxy)
    def statefulset(self) -> StatefulSet:
        return self._origin.statefulset

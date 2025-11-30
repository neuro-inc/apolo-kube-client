from .._models import (
    V1ClusterRole,
    V1ClusterRoleBinding,
    V1ClusterRoleBindingList,
    V1ClusterRoleList,
    V1Status,
)
from .._rbac_authorization_k8s_io_v1 import (
    ClusterRole,
    ClusterRoleBinding,
    RbacAuthorizationK8sIoV1Api,
)
from ._attr_proxy import attr
from ._resource_proxy import BaseProxy, ClusterScopedResourceProxy


class ClusterRoleProxy(
    ClusterScopedResourceProxy[V1ClusterRole, V1ClusterRoleList, V1Status, ClusterRole]
):
    pass


class ClusterRoleBindingProxy(
    ClusterScopedResourceProxy[
        V1ClusterRoleBinding,
        V1ClusterRoleBindingList,
        V1Status,
        ClusterRoleBinding,
    ]
):
    pass


class RbacAuthorizationK8sIoV1ApiProxy(BaseProxy[RbacAuthorizationK8sIoV1Api]):
    """
    rbac.authorization.k8s.io v1 API wrapper for Kubernetes.
    """

    @attr(ClusterRoleProxy)
    def cluster_role(self) -> ClusterRole:
        return self._origin.cluster_role

    @attr(ClusterRoleBindingProxy)
    def cluster_role_binding(self) -> ClusterRoleBinding:
        return self._origin.cluster_role_binding

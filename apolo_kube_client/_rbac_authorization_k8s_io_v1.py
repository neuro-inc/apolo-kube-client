from ._attr import _Attr
from ._base_resource import Base, ClusterScopedResource
from ._models import (
    V1ClusterRole,
    V1ClusterRoleBinding,
    V1ClusterRoleBindingList,
    V1ClusterRoleList,
    V1Status,
)


class ClusterRole(ClusterScopedResource[V1ClusterRole, V1ClusterRoleList, V1Status]):
    query_path = "clusterroles"


class ClusterRoleBinding(
    ClusterScopedResource[V1ClusterRoleBinding, V1ClusterRoleBindingList, V1Status]
):
    query_path = "clusterrolebindings"


class RbacAuthorizationK8sIoV1Api(Base):
    """
    RbacAuthorizationK8sIo v1 API wrapper for Kubernetes.
    """

    group_api_query_path = "apis/rbac.authorization.k8s.io/v1"

    cluster_role = _Attr(ClusterRole, group_api_query_path)
    cluster_role_binding = _Attr(ClusterRoleBinding, group_api_query_path)

from kubernetes.client import ApiClient
from kubernetes.client.models import (
    V1Namespace,
    V1NamespaceList,
    V1Node,
    V1NodeList,
    V1Pod,
    V1PodList,
)

from apolo_kube_client._core import _KubeCore

from ._base_resource import ClusterScopedResource, NamespacedResource


class CoreV1Api:
    """
    Core v1 API wrapper for Kubernetes.
    """

    group_api_query_path = "api/v1"

    def __init__(self, core: _KubeCore, api_client: ApiClient) -> None:
        self._core = core
        self.pod = Pod(core, self.group_api_query_path, api_client)
        self.namespace = Namespace(core, self.group_api_query_path, api_client)
        self.node = Node(core, self.group_api_query_path, api_client)


class Namespace(ClusterScopedResource[V1Namespace, V1NamespaceList, V1Namespace]):
    query_path = "namespaces"


class Pod(NamespacedResource[V1Pod, V1PodList, V1Pod]):
    query_path = "pods"


class Node(ClusterScopedResource[V1Node, V1NodeList, V1Node]):
    query_path = "nodes"

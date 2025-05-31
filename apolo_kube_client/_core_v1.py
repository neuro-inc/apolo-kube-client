from kubernetes.client.models import V1Namespace, V1NamespaceList

from apolo_kube_client._core import _KubeCore

from ._base_resource import NotNamespacedResource


class CoreV1Api:
    """
    Core v1 API wrapper for Kubernetes.
    """

    group_api_query_path = "api/v1"

    def __init__(self, core: _KubeCore) -> None:
        self._core = core

        self.namespace = Namespace(core, self.group_api_query_path)


class Namespace(NotNamespacedResource):
    query_path = "namespaces"
    model = V1Namespace
    list_model = V1NamespaceList

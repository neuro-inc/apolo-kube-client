from kubernetes.client.models import (
    V1Namespace,
    V1NamespaceList,
    V1Node,
    V1NodeList,
    V1Pod,
    V1PodList,
    V1Secret,
    V1SecretList,
    V1Status,
)

from ._base_resource import ClusterScopedResource, NamespacedResource
from ._core import _KubeCore
from ._utils import base64_encode, escape_json_pointer


class CoreV1Api:
    """
    Core v1 API wrapper for Kubernetes.
    """

    group_api_query_path = "api/v1"

    def __init__(self, core: _KubeCore) -> None:
        self._core = core
        # cluster scoped resources
        self.namespace = Namespace(core, self.group_api_query_path)
        self.node = Node(core, self.group_api_query_path)
        # namespaced resources
        self.pod = Pod(core, self.group_api_query_path)
        self.secret = Secret(core, self.group_api_query_path)


class Namespace(ClusterScopedResource[V1Namespace, V1NamespaceList, V1Namespace]):
    query_path = "namespaces"


class Node(ClusterScopedResource[V1Node, V1NodeList, V1Status]):
    query_path = "nodes"


class Pod(NamespacedResource[V1Pod, V1PodList, V1Pod]):
    query_path = "pods"


class Secret(NamespacedResource[V1Secret, V1SecretList, V1Status]):
    query_path = "secrets"

    async def add_key(
        self,
        name: str,
        key: str,
        value: str,
        *,
        namespace: str,
        encode: bool = True,
    ) -> V1Secret:
        secret = await self.get(name=name, namespace=self._get_ns(namespace))
        patch_json_list = []
        if secret.data is None:
            patch_json_list.append({"op": "add", "path": "/data", "value": {}})
        patch_json_list.append(
            {
                "op": "add",
                "path": f"/data/{escape_json_pointer(key)}",
                "value": base64_encode(value) if encode else value,
            }
        )
        return await self.patch_json(
            name=name,
            patch_json_list=patch_json_list,
            namespace=self._get_ns(namespace),
        )

    async def delete_key(self, name: str, key: str, *, namespace: str) -> V1Secret:
        return await self.patch_json(
            name=name,
            patch_json_list=[
                {"op": "remove", "path": f"/data/{escape_json_pointer(key)}"}
            ],
            namespace=self._get_ns(namespace),
        )

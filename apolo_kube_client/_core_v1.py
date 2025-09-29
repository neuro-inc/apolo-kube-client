from kubernetes.client.models import (
    V1Namespace,
    V1NamespaceList,
    V1Node,
    V1NodeList,
    V1PersistentVolume,
    V1PersistentVolumeClaim,
    V1PersistentVolumeClaimList,
    V1PersistentVolumeList,
    V1Pod,
    V1PodList,
    V1Secret,
    V1SecretList,
    V1Status,
)

from ._attr import _Attr
from ._base_resource import Base, ClusterScopedResource, NamespacedResource
from ._utils import base64_encode, escape_json_pointer


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


class PersistentVolume(
    ClusterScopedResource[
        V1PersistentVolume, V1PersistentVolumeList, V1PersistentVolume
    ]
):
    query_path = "persistentvolumes"


class PersistentVolumeClaim(
    NamespacedResource[
        V1PersistentVolumeClaim, V1PersistentVolumeClaimList, V1PersistentVolumeClaim
    ]
):
    query_path = "persistentvolumeclaims"


class CoreV1Api(Base):
    """
    Core v1 API wrapper for Kubernetes.
    """

    group_api_query_path = "api/v1"
    # cluster scoped resources
    namespace = _Attr(Namespace, group_api_query_path)
    node = _Attr(Node, group_api_query_path)
    persistent_volume = _Attr(PersistentVolume, group_api_query_path)
    # namespaced resources
    pod = _Attr(Pod, group_api_query_path)
    secret = _Attr(Secret, group_api_query_path)
    persistent_volume_claim = _Attr(PersistentVolumeClaim, group_api_query_path)

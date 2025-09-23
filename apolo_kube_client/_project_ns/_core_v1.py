from kubernetes.client.models import (
    V1Pod,
    V1PodList,
    V1Secret,
    V1SecretList,
    V1Status,
)

from .._attr import _Attr
from .._core import _KubeCore
from .._core_v1 import CoreV1Api, Pod, Secret
from ._base import ProjectResource


class PrPod(ProjectResource[V1Pod, V1PodList, V1Pod, Pod]):
    pass


class PrSecret(ProjectResource[V1Secret, V1SecretList, V1Status, Secret]):
    async def add_key(
        self,
        name: str,
        key: str,
        value: str,
        *,
        encode: bool = True,
    ) -> V1Secret:
        return await self._origin.add_key(
            name=name, key=key, value=value, encode=encode, namespace=self._namespace
        )

    async def delete_key(self, name: str, key: str) -> V1Secret:
        return await self._origin.delete_key(
            name=name,
            key=key,
            namespace=self._namespace,
        )


class PrCoreV1Api:
    """
    Core v1 API wrapper for Kubernetes.
    """

    group_api_query_path = CoreV1Api.group_api_query_path

    # cluster scoped resources
    # namespaced resources
    pod = _Attr(PrPod, group_api_query_path)
    secret = _Attr(PrSecret, group_api_query_path)

    # ASvetlov: CoreV1Api has cluster-scoped networking_k8s_io_v1 and discovery_k8s_io_v1
    # Not sure if we should expose these attrs in project-scoped client.
    # Most likely it doesn't make any sense.
    # Anyway, we could add them later.

    def __init__(self, core: _KubeCore, namespace: str) -> None:
        self._core = core
        self._namespace = namespace

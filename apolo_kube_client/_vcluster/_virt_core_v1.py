from kubernetes.client.models import (
    V1Pod,
    V1PodList,
    V1Secret,
    V1SecretList,
    V1Status,
)

from .._core_v1 import CoreV1Api, Pod, Secret
from ._virt_attr import attr
from ._virt_base_resource import Base, VirtualResource


class VirtPod(VirtualResource[V1Pod, V1PodList, V1Pod, Pod]):
    pass


class VirtSecret(VirtualResource[V1Secret, V1SecretList, V1Status, Secret]):
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


class VirtCoreV1Api(Base[CoreV1Api]):
    """
    Core v1 API wrapper for Kubernetes.
    """

    # cluster scoped resources
    # namespaced resources
    @attr(VirtPod)
    def pod(self) -> Pod:
        return self._origin.pod

    @attr(VirtSecret)
    def secret(self) -> Secret:
        return self._origin.secret

    # ASvetlov: CoreV1Api has cluster-scoped networking_k8s_io_v1 and discovery_k8s_io_v1
    # Not sure if we should expose these attrs in project-scoped client.
    # Most likely it doesn't make any sense.
    # Anyway, we could add them later.

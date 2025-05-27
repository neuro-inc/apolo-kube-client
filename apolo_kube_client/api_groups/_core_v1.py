from kubernetes.client.models import V1Namespace, V1NamespaceList, V1Status
from yarl import URL

from apolo_kube_client.client import BaseKubeAPIGroup


class CoreV1Api(BaseKubeAPIGroup):
    """
    Core v1 API wrapper for Kubernetes.
    """

    @property
    def api_core_v1_url(self) -> URL:
        return self.kube_client.base_url / "api" / "v1"

    @property
    def namespaces_url(self) -> URL:
        return self.api_core_v1_url / "namespaces"

    def namespace_url(self, namespace: str | None) -> URL:
        namespace = namespace or self.kube_client.namespace
        return self.namespaces_url / namespace

    async def get_namespace(self, name: str) -> V1Namespace:
        url = self.namespace_url(name)
        resp = await self.kube_client.get(url=url)
        return self.kube_client.deserialize(resp, V1Namespace)

    async def get_namespaces(self) -> V1NamespaceList:
        resp = await self.kube_client.get(self.namespaces_url)
        return self.kube_client.deserialize(resp, V1NamespaceList)

    async def create_namespace(self, namespace: V1Namespace) -> V1Namespace:
        resp = await self.kube_client.post(
            url=self.namespaces_url, json=namespace.to_dict()
        )
        return self.kube_client.deserialize(resp, V1Namespace)

    async def delete_namespace(self, name: str) -> V1Status:
        url = self.namespace_url(name)
        resp = await self.kube_client.delete(url)
        return self.kube_client.deserialize(resp, V1Status)

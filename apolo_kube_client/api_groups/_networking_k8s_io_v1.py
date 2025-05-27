from kubernetes.client.models import V1NetworkPolicy
from yarl import URL

from apolo_kube_client.client import BaseKubeAPIGroup


class NetworkingK8SioV1Api(BaseKubeAPIGroup):
    """
    Batch v1 API wrapper for Kubernetes.
    """

    @property
    def api_networking_k8s_io_v1_url(self) -> URL:
        return self.kube_client.base_url / "apis" / "networking.k8s.io" / "v1"

    def api_networking_k8s_io_v1_namespaced_url(
        self, namespace: str | None = None
    ) -> URL:
        namespace = namespace or self.kube_client.namespace
        return self.api_networking_k8s_io_v1_url / "namespaces" / namespace

    def namespaced_network_policies_url(self, namespace: str | None = None) -> URL:
        return (
            self.api_networking_k8s_io_v1_namespaced_url(namespace) / "networkpolicies"
        )

    def namespaced_network_policy_url(
        self, name: str, namespace: str | None = None
    ) -> URL:
        return self.namespaced_network_policies_url(namespace) / name

    async def create_network_policy(
        self, network_policy: V1NetworkPolicy, namespace: str | None = None
    ) -> V1NetworkPolicy:
        url = self.namespaced_network_policies_url(namespace)
        resp = await self.kube_client.post(url=url, json=network_policy.to_dict())
        return self.kube_client.deserialize(resp, V1NetworkPolicy)

    async def get_network_policy(
        self, name: str, namespace: str | None = None
    ) -> V1NetworkPolicy:
        url = self.namespaced_network_policy_url(name, namespace)
        resp = await self.kube_client.get(url=url)
        return self.kube_client.deserialize(resp, V1NetworkPolicy)

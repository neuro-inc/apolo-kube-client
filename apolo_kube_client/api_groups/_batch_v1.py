from kubernetes.client.models import V1Job
from yarl import URL

from apolo_kube_client.client import BaseKubeAPIGroup


class BatchV1Api(BaseKubeAPIGroup):
    """
    Batch v1 API wrapper for Kubernetes.
    """

    @property
    def api_batch_v1_url(self) -> URL:
        return self.kube_client.base_url / "apis" / "batch" / "v1"

    def api_batch_v1_namespaced_url(self, namespace: str | None = None) -> URL:
        namespace = namespace or self.kube_client.namespace
        return self.api_batch_v1_url / "namespaces" / namespace

    def namespaced_jobs_url(self, namespace: str | None = None) -> URL:
        return self.api_batch_v1_namespaced_url(namespace) / "jobs"

    def namespaced_job_url(self, name: str, namespace: str | None = None) -> URL:
        return self.namespaced_jobs_url(namespace) / name

    async def get_job(self, name: str, namespace: str | None = None) -> V1Job:
        url = self.namespaced_job_url(name, namespace)
        resp = await self.kube_client.get(url=url)
        return self.kube_client.deserialize(resp, V1Job)

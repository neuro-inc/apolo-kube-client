from kubernetes.client.models import V1Job, V1JobList

from .._batch_v1 import BatchV1Api, Job
from ._attr_proxy import attr
from ._resource_proxy import BaseProxy, NamespacedResourceProxy


class JobProxy(NamespacedResourceProxy[V1Job, V1JobList, V1Job, Job]):
    pass


class BatchV1ApiProxy(BaseProxy[BatchV1Api]):
    """
    Batch v1 API wrapper for Kubernetes.
    """

    @attr(JobProxy)
    def job(self) -> Job:
        return self._origin.job

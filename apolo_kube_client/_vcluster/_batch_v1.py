from kubernetes.client.models import V1Job, V1JobList

from .._batch_v1 import BatchV1Api, Job
from ._attr import attr
from ._base_resource import Base, VirtualResource


class VJob(VirtualResource[V1Job, V1JobList, V1Job, Job]):
    pass


class VBatchV1Api(Base[BatchV1Api]):
    """
    Batch v1 API wrapper for Kubernetes.
    """

    @attr(VJob)
    def job(self) -> Job:
        return self._origin.job

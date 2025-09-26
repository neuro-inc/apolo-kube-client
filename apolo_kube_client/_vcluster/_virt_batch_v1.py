from kubernetes.client.models import V1Job, V1JobList

from .._batch_v1 import BatchV1Api, Job
from ._virt_attr import attr
from ._virt_base_resource import Base, VirtualResource


class VirtJob(VirtualResource[V1Job, V1JobList, V1Job, Job]):
    pass


class VirtBatchV1Api(Base[BatchV1Api]):
    """
    Batch v1 API wrapper for Kubernetes.
    """

    @attr(VirtJob)
    def job(self) -> Job:
        return self._origin.job

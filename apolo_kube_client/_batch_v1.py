from kubernetes.client.models import V1Job, V1JobList

from ._base_resource import NamespacedResource
from ._core import _KubeCore


class BatchV1Api:
    """
    Batch v1 API wrapper for Kubernetes.
    """

    group_api_query_path = "apis/batch/v1"

    def __init__(self, core: _KubeCore) -> None:
        self._core = core
        self.job = Job(core, self.group_api_query_path)


class Job(NamespacedResource[V1Job, V1JobList, V1Job]):
    query_path = "jobs"

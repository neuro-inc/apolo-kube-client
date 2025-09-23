from kubernetes.client.models import V1Job, V1JobList

from .._batch import BatchV1Api, Job
from ._attr import _Attr
from ._base_resource import NamespacedResource
from ._core import _KubeCore


class PrJob(NamespacedResource[V1Job, V1JobList, V1Job, Job]):
    pass


class PrBatchV1Api:
    """
    Batch v1 API wrapper for Kubernetes.
    """

    group_api_query_path = BatchV1Api.group_api_query_path

    job = _Attr(PrJob, group_api_query_path)

    def __init__(self, core: _KubeCore, namespace: str) -> None:
        self._core = core
        self._namespace = namespace

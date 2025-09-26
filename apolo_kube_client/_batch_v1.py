from kubernetes.client.models import V1Job, V1JobList

from ._attr import _Attr
from ._base_resource import Base, NamespacedResource


class Job(NamespacedResource[V1Job, V1JobList, V1Job]):
    query_path = "jobs"


class BatchV1Api(Base):
    """
    Batch v1 API wrapper for Kubernetes.
    """

    group_api_query_path = "apis/batch/v1"

    job = _Attr(Job, group_api_query_path)

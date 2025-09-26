from unittest.mock import AsyncMock, Mock

from kubernetes.client.models import V1Job

from apolo_kube_client._batch_v1 import BatchV1Api
from apolo_kube_client._vcluster._virt_batch_v1 import VirtBatchV1Api


async def test_virtual_proxy() -> None:
    orig_batch = Mock(spec=BatchV1Api)
    job = V1Job()
    orig_batch.job.get = AsyncMock(return_value=job)
    batch = VirtBatchV1Api(orig_batch, "ns")

    ret = await batch.job.get("name")
    assert ret is job

    orig_batch.job.get.assert_called_once_with(name="name", namespace="ns")

from unittest.mock import AsyncMock, Mock

from apolo_kube_client._batch_v1 import BatchV1Api
from apolo_kube_client._vcluster._batch_v1_proxy import BatchV1ApiProxy
from apolo_kube_client.models import V1Job


async def test_virtual_proxy() -> None:
    orig_batch = Mock(spec=BatchV1Api)
    job = V1Job()
    orig_batch.job.get = AsyncMock(return_value=job)
    batch = BatchV1ApiProxy(orig_batch, "ns")

    ret = await batch.job.get("name")
    assert ret is job

    orig_batch.job.get.assert_called_once_with(name="name", namespace="ns")

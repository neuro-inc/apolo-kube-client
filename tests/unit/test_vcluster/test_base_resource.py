from unittest.mock import AsyncMock, Mock

from apolo_kube_client._batch_v1 import BatchV1Api
from apolo_kube_client._vcluster._batch_v1_proxy import BatchV1ApiProxy
from apolo_kube_client._core_v1 import CoreV1Api
from apolo_kube_client._vcluster._core_v1_proxy import CoreV1ApiProxy
from apolo_kube_client import V1ConfigMap, V1Job


async def test_virtual_proxy() -> None:
    orig_batch = Mock(spec=BatchV1Api)
    job = V1Job()
    orig_batch.job.get = AsyncMock(return_value=job)
    batch = BatchV1ApiProxy(orig_batch, "ns", is_vcluster=False)

    ret = await batch.job.get("name")
    assert ret is job

    orig_batch.job.get.assert_called_once_with(name="name", namespace="ns")


async def test_config_map_proxy() -> None:
    origin_core = Mock(spec=CoreV1Api)
    config_map = V1ConfigMap()
    origin_core.config_map.get = AsyncMock(return_value=config_map)
    origin_core.config_map.add_key = AsyncMock(return_value=config_map)
    origin_core.config_map.delete_key = AsyncMock(return_value=config_map)
    proxy = CoreV1ApiProxy(origin_core, "ns", is_vcluster=False)

    ret = await proxy.config_map.get("name")
    assert ret is config_map
    origin_core.config_map.get.assert_called_once_with(name="name", namespace="ns")

    await proxy.config_map.add_key(name="name", key="k", value="v")
    origin_core.config_map.add_key.assert_called_once_with(
        name="name",
        key="k",
        value="v",
        namespace="ns",
    )

    await proxy.config_map.delete_key(name="name", key="k")
    origin_core.config_map.delete_key.assert_called_once_with(
        name="name",
        key="k",
        namespace="ns",
    )

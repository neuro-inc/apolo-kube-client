from types import TracebackType
from typing import Self

from .._batch_v1 import BatchV1Api
from .._client import KubeClient
from .._core_v1 import CoreV1Api
from .._discovery_k8s_io_v1 import DiscoveryK8sIoV1Api
from .._networking_k8s_io_v1 import NetworkingK8SioV1Api
from ._attr import attr
from ._base_resource import Base
from ._batch_v1 import VBatchV1Api
from ._core_v1 import VCoreV1Api
from ._discovery_k8s_io_v1 import VDiscoveryK8sIoV1Api
from ._networking_k8s_io_v1 import VNetworkingK8SioV1Api


class VKubeClient(Base[KubeClient]):
    @attr(VCoreV1Api)
    def core_v1(self) -> CoreV1Api:
        return self._origin.core_v1

    @attr(VBatchV1Api)
    def batch_v1(self) -> BatchV1Api:
        return self._origin.batch_v1

    @attr(VNetworkingK8SioV1Api)
    def networking_k8s_io_v1(self) -> NetworkingK8SioV1Api:
        return self._origin.networking_k8s_io_v1

    @attr(VDiscoveryK8sIoV1Api)
    def discovery_k8s_io_v1(self) -> DiscoveryK8sIoV1Api:
        return self._origin.discovery_k8s_io_v1

    async def __aenter__(self) -> Self:
        await self._origin.__aenter__()
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        await self._origin.__aexit__(exc_type=exc_type, exc_val=exc_val, exc_tb=exc_tb)

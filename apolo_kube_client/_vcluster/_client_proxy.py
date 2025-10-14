from types import TracebackType
from typing import Self

from .._batch_v1 import BatchV1Api
from .._client import KubeClient
from .._core_v1 import CoreV1Api
from .._discovery_k8s_io_v1 import DiscoveryK8sIoV1Api
from .._networking_k8s_io_v1 import NetworkingK8SioV1Api
from .._neuromation_io_v1 import NeuromationioV1API
from ._attr_proxy import attr
from ._batch_v1_proxy import BatchV1ApiProxy
from ._core_v1_proxy import CoreV1ApiProxy
from ._discovery_k8s_io_v1_proxy import DiscoveryK8sIoV1ApiProxy
from ._networking_k8s_io_v1_proxy import NetworkingK8SioV1ApiProxy
from ._neuromation_io_v1_proxy import NeuromationioV1APIProxy
from ._resource_proxy import BaseProxy


class KubeClientProxy(BaseProxy[KubeClient]):
    @attr(CoreV1ApiProxy)
    def core_v1(self) -> CoreV1Api:
        return self._origin.core_v1

    @attr(BatchV1ApiProxy)
    def batch_v1(self) -> BatchV1Api:
        return self._origin.batch_v1

    @attr(NetworkingK8SioV1ApiProxy)
    def networking_k8s_io_v1(self) -> NetworkingK8SioV1Api:
        return self._origin.networking_k8s_io_v1

    @attr(DiscoveryK8sIoV1ApiProxy)
    def discovery_k8s_io_v1(self) -> DiscoveryK8sIoV1Api:
        return self._origin.discovery_k8s_io_v1

    @attr(NeuromationioV1APIProxy)
    def neuromation_io_v1(self) -> NeuromationioV1API:
        return self._origin.neuromation_io_v1

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

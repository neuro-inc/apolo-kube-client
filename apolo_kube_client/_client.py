import logging
from types import TracebackType
from typing import Self

from ._admissionregistration_k8s_io_v1 import AdmissionRegistrationK8SioV1Api
from ._apiextensions_k8s_io_v1 import ExtensionsK8sV1Api
from ._apps_v1 import AppsV1Api
from ._attr import _Attr
from ._batch_v1 import BatchV1Api
from ._config import KubeConfig
from ._core import _KubeCore
from ._core_v1 import CoreV1Api
from ._discovery_k8s_io_v1 import DiscoveryK8sIoV1Api
from ._networking_k8s_io_v1 import NetworkingK8SioV1Api
from ._neuromation_io_v1 import NeuromationioV1API
from ._resource_list import ResourceListApi
from ._storage_k8s_io_v1 import StorageK8SioV1Api
from ._transport import KubeTransport

logger = logging.getLogger(__name__)


class KubeClient:
    resource_list = _Attr(ResourceListApi)
    core_v1 = _Attr(CoreV1Api)
    apps_v1 = _Attr(AppsV1Api)
    batch_v1 = _Attr(BatchV1Api)
    networking_k8s_io_v1 = _Attr(NetworkingK8SioV1Api)
    admission_registration_k8s_io_v1 = _Attr(AdmissionRegistrationK8SioV1Api)
    discovery_k8s_io_v1 = _Attr(DiscoveryK8sIoV1Api)
    storage_k8s_io_v1 = _Attr(StorageK8SioV1Api)
    neuromation_io_v1 = _Attr(NeuromationioV1API)
    extensions_k8s_io_v1 = _Attr(ExtensionsK8sV1Api)

    def __init__(
        self,
        *,
        config: KubeConfig,
        transport: KubeTransport | None = None,
    ) -> None:
        self._config = config
        self._owns_transport = transport is None
        if transport is None:
            transport = KubeTransport(
                conn_pool_size=config.client_conn_pool_size,
                conn_timeout_s=config.client_conn_timeout_s,
                read_timeout_s=config.client_read_timeout_s,
            )
        self._transport = transport
        self._core = _KubeCore(config, transport=transport)

    async def __aenter__(self) -> Self:
        if self._owns_transport:
            await self._transport.__aenter__()
        await self._core.__aenter__()
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        await self._core.__aexit__(exc_type=exc_type, exc_val=exc_val, exc_tb=exc_tb)
        if self._owns_transport:
            await self._transport.__aexit__(
                exc_type=exc_type, exc_val=exc_val, exc_tb=exc_tb
            )

    @property
    def namespace(self) -> str:
        """
        Returns the current namespace of the Kubernetes client.
        """
        return self._core.resolve_namespace()

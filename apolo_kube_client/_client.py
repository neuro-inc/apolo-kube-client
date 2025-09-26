import logging
from types import TracebackType
from typing import Self

from ._admissionregistration_k8s_io_v1 import AdmissionRegistrationK8SioV1Api
from ._attr import _Attr
from ._batch_v1 import BatchV1Api
from ._config import KubeConfig
from ._core import _KubeCore
from ._core_v1 import CoreV1Api
from ._discovery_k8s_io_v1 import DiscoveryK8sIoV1Api
from ._networking_k8s_io_v1 import NetworkingK8SioV1Api
from ._resource_list import ResourceListApi

logger = logging.getLogger(__name__)


class KubeClient:
    resource_list = _Attr(ResourceListApi)
    core_v1 = _Attr(CoreV1Api)
    batch_v1 = _Attr(BatchV1Api)
    networking_k8s_io_v1 = _Attr(NetworkingK8SioV1Api)
    admission_registration_k8s_io_v1 = _Attr(AdmissionRegistrationK8SioV1Api)
    discovery_k8s_io_v1 = _Attr(DiscoveryK8sIoV1Api)

    def __init__(self, *, config: KubeConfig) -> None:
        self._config = config
        self._core = _KubeCore(config)

    async def __aenter__(self) -> Self:
        await self._core.__aenter__()
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        await self._core.__aexit__(exc_type=exc_type, exc_val=exc_val, exc_tb=exc_tb)

    @property
    def namespace(self) -> str:
        """
        Returns the current namespace of the Kubernetes client.
        """
        return self._core.resolve_namespace()

    @property
    def config(self) -> KubeConfig:
        """Return a copy of the configuration used to instantiate the client."""
        return self._config.model_copy()

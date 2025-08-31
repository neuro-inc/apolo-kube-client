import logging
from types import TracebackType
from typing import Self

from ._admissionregistration_k8s_io_v1 import AdmissionRegistrationK8SioV1Api
from ._batch_v1 import BatchV1Api
from ._config import KubeConfig
from ._core import _KubeCore
from ._core_v1 import CoreV1Api
from ._discovery_k8s_io_v1 import DiscoveryK8sIoV1Api
from ._networking_k8s_io_v1 import NetworkingK8SioV1Api
from ._resource_list import ResourceListApi

logger = logging.getLogger(__name__)


class KubeClient:
    def __init__(self, *, config: KubeConfig) -> None:
        self._core = _KubeCore(config)

        self.resource_list = ResourceListApi(self._core)
        self.core_v1 = CoreV1Api(self._core)
        self.batch_v1 = BatchV1Api(self._core)
        self.networking_k8s_io_v1 = NetworkingK8SioV1Api(self._core)
        self.admission_registration_k8s_io_v1 = AdmissionRegistrationK8SioV1Api(
            self._core
        )
        self.discovery_k8s_io_v1 = DiscoveryK8sIoV1Api(self._core)

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
        return self._core.namespace

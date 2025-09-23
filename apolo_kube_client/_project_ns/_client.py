from ._admissionregistration_k8s_io_v1 import AdmissionRegistrationK8SioV1Api
from ._batch_v1 import BatchV1Api
from .._config import KubeConfig
from .._core import _KubeCore
from ._core_v1 import CoreV1Api
from ._discovery_k8s_io_v1 import DiscoveryK8sIoV1Api
from ._networking_k8s_io_v1 import NetworkingK8SioV1Api
from ._resource_list import ResourceListApi
from ..apolo import generate_namespace_name



class PrKubeClient:
    def __init__(self, *, config: KubeConfig
                         *,
        is_vcluster: bool,
        org_name: str,
        project_name: str,
) -> None:
        self._core = _KubeCore(config)

        if is_vcluster:
            namespace = "default"
        else:
            namespace = generate_namespace_name(org_name, project_name)

        self.resource_list = ResourceListApi(self._core, namespace)
        self.core_v1 = CoreV1Api(self._core, namespace)
        self.batch_v1 = BatchV1Api(self._core, namespace)
        self.networking_k8s_io_v1 = NetworkingK8SioV1Api(self._core, namespace)
        self.admission_registration_k8s_io_v1 = AdmissionRegistrationK8SioV1Api(
            self._core, namespace
        )
        self.discovery_k8s_io_v1 = DiscoveryK8sIoV1Api(self._core, namespace)

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

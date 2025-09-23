from types import TracebackType
from typing import Self

from .._attr import _Attr
from .._core import _KubeCore
from ..apolo import generate_namespace_name
from ._batch_v1 import PrBatchV1Api
from ._core_v1 import PrCoreV1Api
from ._discovery_k8s_io_v1 import PrDiscoveryK8sIoV1Api
from ._networking_k8s_io_v1 import PrNetworkingK8SioV1Api


class PrKubeClient:
    core_v1 = _Attr(PrCoreV1Api)
    batch_v1 = _Attr(PrBatchV1Api)
    networking_k8s_io_v1 = _Attr(PrNetworkingK8SioV1Api)
    discovery_k8s_io_v1 = _Attr(PrDiscoveryK8sIoV1Api)

    # TODO: after combining with Selector API the signature will be changed somehow
    def __init__(
        self,
        core: _KubeCore,
        *,
        is_vcluster: bool,
        org_name: str,
        project_name: str,
    ) -> None:
        self._core = core

        if is_vcluster:
            self._namespace = "default"
        else:
            self._namespace = generate_namespace_name(org_name, project_name)

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

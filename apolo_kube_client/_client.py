import logging
from typing import Any

from ._batch_v1 import BatchV1Api
from ._config import KubeConfig
from ._core import _KubeCore
from ._core_v1 import CoreV1Api
from ._networking_k8s_io_v1 import NetworkingK8SioV1Api

logger = logging.getLogger(__name__)


class KubeClient:
    def __init__(self, *, config: KubeConfig) -> None:
        self._core = _KubeCore(config)

        self.core_v1 = CoreV1Api(self._core)
        self.batch_v1 = BatchV1Api(self._core)
        self.networking_k8s_io_v1 = NetworkingK8SioV1Api(self._core)

    async def __aenter__(self) -> "KubeClient":
        async with self._core:
            return self

    async def __aexit__(self, *args: Any) -> None:
        await self._core.close()

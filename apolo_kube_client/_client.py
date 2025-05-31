import logging
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from typing import Optional

import aiohttp

from ._batch_v1 import BatchV1Api
from ._config import KubeConfig
from ._core import _KubeCore
from ._core_v1 import CoreV1Api
from ._networking_k8s_io_v1 import NetworkingK8SioV1Api

logger = logging.getLogger(__name__)


class KubeClient:
    def __init__(self, *, core: _KubeCore) -> None:
        self._core = core

        self.core_v1 = CoreV1Api(self._core)
        self.batch_v1 = BatchV1Api(self._core)
        self.networking_k8s_io_v1 = NetworkingK8SioV1Api(self._core)


@asynccontextmanager
async def create_kube_client(
    config: KubeConfig, trace_configs: Optional[list[aiohttp.TraceConfig]] = None
) -> AsyncIterator[KubeClient]:
    kube_core = _KubeCore(
        base_url=config.endpoint_url,
        namespace=config.namespace,
        cert_authority_path=config.cert_authority_path,
        cert_authority_data_pem=config.cert_authority_data_pem,
        auth_type=config.auth_type,
        auth_cert_path=config.auth_cert_path,
        auth_cert_key_path=config.auth_cert_key_path,
        token=config.token,
        token_path=config.token_path,
        conn_timeout_s=config.client_conn_timeout_s,
        read_timeout_s=config.client_read_timeout_s,
        watch_timeout_s=config.client_watch_timeout_s,
        conn_pool_size=config.client_conn_pool_size,
        trace_configs=trace_configs,
    )
    try:
        await kube_core.init()
        kube_client = KubeClient(core=kube_core)
        yield kube_client
    except Exception as e:
        logger.exception("%s: unhandled error happened", config)
        raise e
    finally:
        await kube_core.close()

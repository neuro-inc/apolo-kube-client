from __future__ import annotations

import logging
import shutil
import tempfile
from pathlib import Path

import yaml
from kubernetes.client.models import V1Secret

from apolo_kube_client._client import KubeClient
from apolo_kube_client._config import KubeClientAuthType, KubeConfig
from apolo_kube_client._transport import KubeTransport
from apolo_kube_client._utils import base64_decode

logger = logging.getLogger(__name__)


class VclusterClientFactory:
    def __init__(
        self,
        default_config: KubeConfig,
        transport: KubeTransport,
    ) -> None:
        self._default_config = default_config
        self._transport = transport
        self._temp_dirs: dict[int, Path] = {}

    async def from_secret(self, secret: V1Secret) -> KubeClient:
        raw_kubeconfig = base64_decode(secret.data["config"])
        yaml_kubeconfig = yaml.safe_load(raw_kubeconfig)

        endpoint_url = yaml_kubeconfig["clusters"][0]["cluster"]["server"]
        ca_pem = base64_decode(secret.data["certificate-authority"])
        cert_pem = base64_decode(secret.data["client-certificate"])
        key_pem = base64_decode(secret.data["client-key"])

        temp_dir = Path(tempfile.mkdtemp(prefix="apolo-kube-client-vc-"))
        cert_path = temp_dir / "client.crt"
        key_path = temp_dir / "client.key"
        cert_path.write_text(cert_pem)
        key_path.write_text(key_pem)

        kube_config = KubeConfig(
            endpoint_url=endpoint_url,
            cert_authority_data_pem=ca_pem,
            auth_type=KubeClientAuthType.CERTIFICATE,
            auth_cert_path=str(cert_path),
            auth_cert_key_path=str(key_path),
            client_conn_timeout_s=self._default_config.client_conn_timeout_s,
            client_read_timeout_s=self._default_config.client_read_timeout_s,
            client_watch_timeout_s=self._default_config.client_watch_timeout_s,
            client_conn_pool_size=self._default_config.client_conn_pool_size,
            token_update_interval_s=self._default_config.token_update_interval_s,
        )
        client = KubeClient(config=kube_config, transport=self._transport)
        await client.__aenter__()
        # Track temp dir for later cleanup
        self._temp_dirs[id(client)] = temp_dir
        return client

    async def close(self, client: KubeClient) -> None:
        try:
            await client.__aexit__(None, None, None)
        except Exception:
            logger.exception("unable to cleanup the client")
        temp_dir = self._temp_dirs.pop(id(client), None)
        if temp_dir is None:
            return
        try:
            shutil.rmtree(temp_dir, ignore_errors=True)
        except Exception:
            logger.exception("unable to remove cert temp dir")

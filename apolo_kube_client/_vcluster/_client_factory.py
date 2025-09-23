from __future__ import annotations

import shutil
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Callable

import yaml
from kubernetes.client.models import V1Secret

from apolo_kube_client._client import KubeClient
from apolo_kube_client._config import NAMESPACE_DEFAULT, KubeClientAuthType, KubeConfig
from apolo_kube_client._utils import base64_decode


@dataclass
class ClientWrapper:
    client: KubeClient
    cleanup: Callable[[], None]


class VclusterClientFactory:
    def __init__(self, default_config: KubeConfig) -> None:
        self._default_config = default_config

    async def from_secret(self, secret: V1Secret) -> ClientWrapper:
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

        def cleanup() -> None:
            """Remove cert dir on a cleanup"""
            shutil.rmtree(temp_dir, ignore_errors=True)

        kube_config = KubeConfig(
            endpoint_url=endpoint_url,
            cert_authority_data_pem=ca_pem,
            auth_type=KubeClientAuthType.CERTIFICATE,
            auth_cert_path=str(cert_path),
            auth_cert_key_path=str(key_path),
            namespace=NAMESPACE_DEFAULT,
            forced_namespace=NAMESPACE_DEFAULT,
            client_conn_timeout_s=self._default_config.client_conn_timeout_s,
            client_read_timeout_s=self._default_config.client_read_timeout_s,
            client_watch_timeout_s=self._default_config.client_watch_timeout_s,
            client_conn_pool_size=self._default_config.client_conn_pool_size,
            token_update_interval_s=self._default_config.token_update_interval_s,
        )

        client = KubeClient(config=kube_config)
        await client.__aenter__()
        return ClientWrapper(client=client, cleanup=cleanup)

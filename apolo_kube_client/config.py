from dataclasses import dataclass, field
from typing import Optional

from apolo_kube_client.client import KubeClientAuthType

NAMESPACE_DEFAULT = "default"


@dataclass(frozen=True)
class KubeConfig:
    endpoint_url: str
    cert_authority_data_pem: Optional[str] = field(repr=False, default=None)
    cert_authority_path: Optional[str] = None
    auth_type: KubeClientAuthType = KubeClientAuthType.NONE
    auth_cert_path: Optional[str] = None
    auth_cert_key_path: Optional[str] = None
    token: Optional[str] = field(repr=False, default=None)
    token_path: Optional[str] = None
    verify_ssl: bool = True
    namespace: str = NAMESPACE_DEFAULT
    client_conn_timeout_s: int = 300
    client_read_timeout_s: int = 300
    client_watch_timeout_s: int = 1800
    client_conn_pool_size: int = 100

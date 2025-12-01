from pydantic import BaseModel, ConfigDict, Field

from ._constants import (
    DEFAULT_AUTH_TYPE,
    DEFAULT_CLIENT_CONN_POOL_SIZE,
    DEFAULT_CLIENT_CONN_TIMEOUT,
    DEFAULT_CLIENT_READ_TIMEOUT,
    DEFAULT_CLIENT_WATCH_TIMEOUT,
    DEFAULT_TOKEN_UPDATE_INTERVAL,
    KubeClientAuthType,
)


class KubeConfig(BaseModel):
    model_config = ConfigDict(frozen=True)

    endpoint_url: str
    cert_authority_data_pem: str | None = Field(repr=False, default=None)
    cert_authority_path: str | None = None
    auth_type: KubeClientAuthType = DEFAULT_AUTH_TYPE
    auth_cert_path: str | None = None
    auth_cert_key_path: str | None = None
    token: str | None = Field(repr=False, default=None)
    token_path: str | None = None
    token_update_interval_s: int = DEFAULT_TOKEN_UPDATE_INTERVAL
    client_conn_timeout_s: int = DEFAULT_CLIENT_CONN_TIMEOUT
    client_read_timeout_s: int = DEFAULT_CLIENT_READ_TIMEOUT
    client_watch_timeout_s: int = DEFAULT_CLIENT_WATCH_TIMEOUT
    client_conn_pool_size: int = DEFAULT_CLIENT_CONN_POOL_SIZE

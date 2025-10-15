from pydantic import BaseModel, Field

from .v1_server_address_by_client_c_i_d_r import V1ServerAddressByClientCIDR


class V1APIVersions(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    kind: str | None = Field(None, alias="kind")

    server_address_by_client_cid_rs: list[V1ServerAddressByClientCIDR] | None = Field(
        None, alias="serverAddressByClientCIDRs"
    )

    versions: list[str] | None = Field(None, alias="versions")

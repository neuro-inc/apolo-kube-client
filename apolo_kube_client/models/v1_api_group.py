from pydantic import BaseModel, Field

from .v1_group_version_for_discovery import V1GroupVersionForDiscovery
from .v1_server_address_by_client_c_i_d_r import V1ServerAddressByClientCIDR


class V1APIGroup(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    kind: str | None = Field(None, alias="kind")

    name: str | None = Field(None, alias="name")

    preferred_version: V1GroupVersionForDiscovery | None = Field(
        None, alias="preferredVersion"
    )

    server_address_by_client_cid_rs: list[V1ServerAddressByClientCIDR] | None = Field(
        None, alias="serverAddressByClientCIDRs"
    )

    versions: list[V1GroupVersionForDiscovery] | None = Field(None, alias="versions")

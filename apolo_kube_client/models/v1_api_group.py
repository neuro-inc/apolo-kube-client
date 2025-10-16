from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_group_version_for_discovery import V1GroupVersionForDiscovery
from .v1_server_address_by_client_cidr import V1ServerAddressByClientCIDR

__all__ = ("V1APIGroup",)


class V1APIGroup(BaseModel):
    api_version: str | None = Field(default_factory=lambda: None, alias="apiVersion")

    kind: str | None = Field(default_factory=lambda: None, alias="kind")

    name: str | None = Field(default_factory=lambda: None, alias="name")

    preferred_version: V1GroupVersionForDiscovery = Field(
        default_factory=lambda: V1GroupVersionForDiscovery(), alias="preferredVersion"
    )

    server_address_by_client_cid_rs: list[V1ServerAddressByClientCIDR] = Field(
        default_factory=lambda: [], alias="serverAddressByClientCIDRs"
    )

    versions: list[V1GroupVersionForDiscovery] = Field(
        default_factory=lambda: [], alias="versions"
    )

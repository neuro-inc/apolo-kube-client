from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_server_address_by_client_cidr import V1ServerAddressByClientCIDR

__all__ = ("V1APIVersions",)


class V1APIVersions(BaseModel):
    api_version: str | None = Field(default_factory=lambda: None, alias="apiVersion")

    kind: str | None = Field(default_factory=lambda: None, alias="kind")

    server_address_by_client_cid_rs: list[V1ServerAddressByClientCIDR] = Field(
        default_factory=lambda: [], alias="serverAddressByClientCIDRs"
    )

    versions: list[str] = Field(default_factory=lambda: [], alias="versions")

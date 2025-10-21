from pydantic import AliasChoices, BaseModel, Field
from .base import _default_if_none
from .v1_group_version_for_discovery import V1GroupVersionForDiscovery
from .v1_server_address_by_client_cidr import V1ServerAddressByClientCIDR
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1APIGroup",)


class V1APIGroup(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    kind: str | None = None

    name: str | None = None

    preferred_version: Annotated[
        V1GroupVersionForDiscovery,
        BeforeValidator(_default_if_none(V1GroupVersionForDiscovery)),
    ] = Field(
        default_factory=lambda: V1GroupVersionForDiscovery(),
        serialization_alias="preferredVersion",
        validation_alias=AliasChoices("preferred_version", "preferredVersion"),
    )

    server_address_by_client_cid_rs: list[V1ServerAddressByClientCIDR] = Field(
        default=[],
        serialization_alias="serverAddressByClientCIDRs",
        validation_alias=AliasChoices(
            "server_address_by_client_cid_rs", "serverAddressByClientCIDRs"
        ),
    )

    versions: list[V1GroupVersionForDiscovery] = []

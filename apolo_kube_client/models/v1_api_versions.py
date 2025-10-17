from pydantic import AliasChoices, BaseModel, Field
from .v1_server_address_by_client_cidr import V1ServerAddressByClientCIDR

__all__ = ("V1APIVersions",)


class V1APIVersions(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    kind: str | None = None

    server_address_by_client_cid_rs: list[V1ServerAddressByClientCIDR] = Field(
        default=[],
        serialization_alias="serverAddressByClientCIDRs",
        validation_alias=AliasChoices(
            "server_address_by_client_cid_rs", "serverAddressByClientCIDRs"
        ),
    )

    versions: list[str] = []

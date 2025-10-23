from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .utils import _exclude_if
from .v1_server_address_by_client_cidr import V1ServerAddressByClientCIDR
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1APIVersions",)


class V1APIVersions(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
        exclude_if=_exclude_if,
    )

    kind: str | None = Field(default=None, exclude_if=_exclude_if)

    server_address_by_client_cid_rs: Annotated[
        list[V1ServerAddressByClientCIDR], BeforeValidator(_collection_if_none("[]"))
    ] = Field(
        default=[],
        serialization_alias="serverAddressByClientCIDRs",
        validation_alias=AliasChoices(
            "server_address_by_client_cid_rs", "serverAddressByClientCIDRs"
        ),
        exclude_if=_exclude_if,
    )

    versions: Annotated[list[str], BeforeValidator(_collection_if_none("[]"))] = Field(
        default=[], exclude_if=_exclude_if
    )

from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_list_meta import V1ListMeta
from .v1beta1_ip_address import V1beta1IPAddress

__all__ = ("V1beta1IPAddressList",)


class V1beta1IPAddressList(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    items: list[V1beta1IPAddress] = Field(default=[])

    kind: str | None = Field(default=None)

    metadata: V1ListMeta

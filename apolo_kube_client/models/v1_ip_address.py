from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_ip_address_spec import V1IPAddressSpec
from .v1_object_meta import V1ObjectMeta

__all__ = ("V1IPAddress",)


class V1IPAddress(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    kind: str | None = Field(default=None)

    metadata: V1ObjectMeta

    spec: V1IPAddressSpec = Field(default_factory=lambda: V1IPAddressSpec())

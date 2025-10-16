from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_ip_address_spec import V1IPAddressSpec
from .v1_object_meta import V1ObjectMeta

__all__ = ("V1IPAddress",)


class V1IPAddress(BaseModel):
    api_version: str | None = Field(default_factory=lambda: None, alias="apiVersion")

    kind: str | None = Field(default_factory=lambda: None, alias="kind")

    metadata: V1ObjectMeta = Field(
        default_factory=lambda: V1ObjectMeta(), alias="metadata"
    )

    spec: V1IPAddressSpec = Field(
        default_factory=lambda: V1IPAddressSpec(), alias="spec"
    )

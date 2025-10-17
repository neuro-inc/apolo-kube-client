from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_list_meta import V1ListMeta
from .v1beta1_ip_address import V1beta1IPAddress

__all__ = ("V1beta1IPAddressList",)


class V1beta1IPAddressList(BaseModel):
    api_version: str | None = Field(default_factory=lambda: None, alias="apiVersion")

    items: list[V1beta1IPAddress] = Field(default_factory=lambda: [])

    kind: str | None = Field(default_factory=lambda: None)

    metadata: V1ListMeta = Field(default_factory=lambda: V1ListMeta())

from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_http_header import V1HTTPHeader
from apolo_kube_client._typedefs import JsonType

__all__ = ("V1HTTPGetAction",)


class V1HTTPGetAction(BaseModel):
    host: str | None = Field(default_factory=lambda: None, alias="host")

    http_headers: list[V1HTTPHeader] = Field(
        default_factory=lambda: [], alias="httpHeaders"
    )

    path: str | None = Field(default_factory=lambda: None, alias="path")

    port: JsonType = Field(default_factory=lambda: {}, alias="port")

    scheme: str | None = Field(default_factory=lambda: None, alias="scheme")

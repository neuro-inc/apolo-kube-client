from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_http_header import V1HTTPHeader
from apolo_kube_client._typedefs import JsonType

__all__ = ("V1HTTPGetAction",)


class V1HTTPGetAction(BaseModel):
    host: str | None = Field(default=None)

    http_headers: list[V1HTTPHeader] = Field(
        default=[],
        serialization_alias="httpHeaders",
        validation_alias=AliasChoices("http_headers", "httpHeaders"),
    )

    path: str | None = Field(default=None)

    port: JsonType = Field(default={})

    scheme: str | None = Field(default=None)

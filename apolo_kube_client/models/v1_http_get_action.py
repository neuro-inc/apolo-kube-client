from __future__ import annotations

from pydantic import BaseModel, Field

from apolo_kube_client._typedefs import JsonType

from .v1_http_header import V1HTTPHeader

__all__ = ("V1HTTPGetAction",)


class V1HTTPGetAction(BaseModel):
    host: str | None = Field(None, alias="host")

    http_headers: list[V1HTTPHeader] | None = Field(None, alias="httpHeaders")

    path: str | None = Field(None, alias="path")

    port: JsonType | None = Field(None, alias="port")

    scheme: str | None = Field(None, alias="scheme")

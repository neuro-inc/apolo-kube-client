from __future__ import annotations
from pydantic import BaseModel, Field
from apolo_kube_client._typedefs import JsonType

__all__ = ("V1TCPSocketAction",)


class V1TCPSocketAction(BaseModel):
    host: str | None = Field(default_factory=lambda: None, alias="host")

    port: JsonType = Field(default_factory=lambda: {}, alias="port")

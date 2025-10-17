from __future__ import annotations
from pydantic import BaseModel, Field
from apolo_kube_client._typedefs import JsonType

__all__ = ("V1ServicePort",)


class V1ServicePort(BaseModel):
    app_protocol: str | None = Field(default_factory=lambda: None, alias="appProtocol")

    name: str | None = Field(default_factory=lambda: None)

    node_port: int | None = Field(default_factory=lambda: None, alias="nodePort")

    port: int | None = Field(default_factory=lambda: None)

    protocol: str | None = Field(default_factory=lambda: None)

    target_port: JsonType = Field(default_factory=lambda: {}, alias="targetPort")

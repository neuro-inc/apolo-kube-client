from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("CoreV1EndpointPort",)


class CoreV1EndpointPort(BaseModel):
    app_protocol: str | None = Field(default_factory=lambda: None, alias="appProtocol")

    name: str | None = Field(default_factory=lambda: None, alias="name")

    port: int | None = Field(default_factory=lambda: None, alias="port")

    protocol: str | None = Field(default_factory=lambda: None, alias="protocol")

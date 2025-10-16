from __future__ import annotations

from pydantic import BaseModel, Field

from .v1_service_backend_port import V1ServiceBackendPort

__all__ = ("V1IngressServiceBackend",)


class V1IngressServiceBackend(BaseModel):
    name: str | None = Field(None, alias="name")

    port: V1ServiceBackendPort | None = Field(None, alias="port")

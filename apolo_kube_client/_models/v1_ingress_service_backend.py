from pydantic import BaseModel, Field
from .v1_service_backend_port import V1ServiceBackendPort

__all__ = ("V1IngressServiceBackend",)


class V1IngressServiceBackend(BaseModel):
    name: str | None = None

    port: V1ServiceBackendPort = Field(default_factory=lambda: V1ServiceBackendPort())

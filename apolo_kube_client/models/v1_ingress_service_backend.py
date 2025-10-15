from pydantic import BaseModel, Field

from .v1_service_backend_port import V1ServiceBackendPort


class V1IngressServiceBackend(BaseModel):
    name: str | None = Field(None, alias="name")

    port: V1ServiceBackendPort | None = Field(None, alias="port")

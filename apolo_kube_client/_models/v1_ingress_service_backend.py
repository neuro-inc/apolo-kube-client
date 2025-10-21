from pydantic import BaseModel, Field
from .base import _default_if_none
from .v1_service_backend_port import V1ServiceBackendPort
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1IngressServiceBackend",)


class V1IngressServiceBackend(BaseModel):
    name: str | None = None

    port: Annotated[
        V1ServiceBackendPort, BeforeValidator(_default_if_none(V1ServiceBackendPort))
    ] = Field(default_factory=lambda: V1ServiceBackendPort())

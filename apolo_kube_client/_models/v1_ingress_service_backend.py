from pydantic import BaseModel, Field
from .utils import _default_if_none
from .utils import _exclude_if
from .v1_service_backend_port import V1ServiceBackendPort
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1IngressServiceBackend",)


class V1IngressServiceBackend(BaseModel):
    name: str | None = Field(default=None, exclude_if=_exclude_if)

    port: Annotated[
        V1ServiceBackendPort, BeforeValidator(_default_if_none(V1ServiceBackendPort))
    ] = Field(default_factory=lambda: V1ServiceBackendPort(), exclude_if=_exclude_if)

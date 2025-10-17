from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_object_meta import V1ObjectMeta
from .v1_service_spec import V1ServiceSpec
from .v1_service_status import V1ServiceStatus

__all__ = ("V1Service",)


class V1Service(BaseModel):
    api_version: str | None = Field(default_factory=lambda: None, alias="apiVersion")

    kind: str | None = Field(default_factory=lambda: None)

    metadata: V1ObjectMeta = Field(default_factory=lambda: V1ObjectMeta())

    spec: V1ServiceSpec = Field(default_factory=lambda: V1ServiceSpec())

    status: V1ServiceStatus = Field(default_factory=lambda: V1ServiceStatus())

from __future__ import annotations

from pydantic import BaseModel, Field

from .v1_object_meta import V1ObjectMeta
from .v1_service_spec import V1ServiceSpec
from .v1_service_status import V1ServiceStatus

__all__ = ("V1Service",)


class V1Service(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ObjectMeta | None = Field(None, alias="metadata")

    spec: V1ServiceSpec | None = Field(None, alias="spec")

    status: V1ServiceStatus | None = Field(None, alias="status")

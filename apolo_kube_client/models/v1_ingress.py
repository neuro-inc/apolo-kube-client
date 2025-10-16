from __future__ import annotations

from pydantic import BaseModel, Field

from .v1_ingress_spec import V1IngressSpec
from .v1_ingress_status import V1IngressStatus
from .v1_object_meta import V1ObjectMeta

__all__ = ("V1Ingress",)


class V1Ingress(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ObjectMeta | None = Field(None, alias="metadata")

    spec: V1IngressSpec | None = Field(None, alias="spec")

    status: V1IngressStatus | None = Field(None, alias="status")

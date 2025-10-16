from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_ingress_spec import V1IngressSpec
from .v1_ingress_status import V1IngressStatus
from .v1_object_meta import V1ObjectMeta

__all__ = ("V1Ingress",)


class V1Ingress(BaseModel):
    api_version: str | None = Field(default_factory=lambda: None, alias="apiVersion")

    kind: str | None = Field(default_factory=lambda: None, alias="kind")

    metadata: V1ObjectMeta = Field(
        default_factory=lambda: V1ObjectMeta(), alias="metadata"
    )

    spec: V1IngressSpec = Field(default_factory=lambda: V1IngressSpec(), alias="spec")

    status: V1IngressStatus = Field(
        default_factory=lambda: V1IngressStatus(), alias="status"
    )

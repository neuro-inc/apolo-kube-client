from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_ingress_spec import V1IngressSpec
from .v1_ingress_status import V1IngressStatus
from .v1_object_meta import V1ObjectMeta

__all__ = ("V1Ingress",)


class V1Ingress(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    kind: str | None = Field(default=None)

    metadata: V1ObjectMeta

    spec: V1IngressSpec = Field(default_factory=lambda: V1IngressSpec())

    status: V1IngressStatus = Field(default_factory=lambda: V1IngressStatus())

from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_ingress_class_spec import V1IngressClassSpec
from .v1_object_meta import V1ObjectMeta

__all__ = ("V1IngressClass",)


class V1IngressClass(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    kind: str | None = Field(default=None)

    metadata: V1ObjectMeta

    spec: V1IngressClassSpec = Field(default_factory=lambda: V1IngressClassSpec())

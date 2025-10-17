from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_ingress_class_spec import V1IngressClassSpec
from .v1_object_meta import V1ObjectMeta

__all__ = ("V1IngressClass",)


class V1IngressClass(BaseModel):
    api_version: str | None = Field(default_factory=lambda: None, alias="apiVersion")

    kind: str | None = Field(default_factory=lambda: None)

    metadata: V1ObjectMeta = Field(default_factory=lambda: V1ObjectMeta())

    spec: V1IngressClassSpec = Field(default_factory=lambda: V1IngressClassSpec())

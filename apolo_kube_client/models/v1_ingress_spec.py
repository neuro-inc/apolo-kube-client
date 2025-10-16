from __future__ import annotations

from pydantic import BaseModel, Field

from .v1_ingress_backend import V1IngressBackend
from .v1_ingress_rule import V1IngressRule
from .v1_ingress_tls import V1IngressTLS

__all__ = ("V1IngressSpec",)


class V1IngressSpec(BaseModel):
    default_backend: V1IngressBackend | None = Field(None, alias="defaultBackend")

    ingress_class_name: str | None = Field(None, alias="ingressClassName")

    rules: list[V1IngressRule] | None = Field(None, alias="rules")

    tls: list[V1IngressTLS] | None = Field(None, alias="tls")

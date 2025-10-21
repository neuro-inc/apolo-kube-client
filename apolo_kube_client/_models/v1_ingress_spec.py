from pydantic import AliasChoices, BaseModel, Field
from .base import _default_if_none
from .v1_ingress_backend import V1IngressBackend
from .v1_ingress_rule import V1IngressRule
from .v1_ingress_tls import V1IngressTLS
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1IngressSpec",)


class V1IngressSpec(BaseModel):
    default_backend: Annotated[
        V1IngressBackend, BeforeValidator(_default_if_none(V1IngressBackend))
    ] = Field(
        default_factory=lambda: V1IngressBackend(),
        serialization_alias="defaultBackend",
        validation_alias=AliasChoices("default_backend", "defaultBackend"),
    )

    ingress_class_name: str | None = Field(
        default=None,
        serialization_alias="ingressClassName",
        validation_alias=AliasChoices("ingress_class_name", "ingressClassName"),
    )

    rules: list[V1IngressRule] = []

    tls: list[V1IngressTLS] = []

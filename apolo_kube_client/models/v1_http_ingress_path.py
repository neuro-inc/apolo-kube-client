from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_ingress_backend import V1IngressBackend

__all__ = ("V1HTTPIngressPath",)


class V1HTTPIngressPath(BaseModel):
    backend: V1IngressBackend = Field(default_factory=lambda: V1IngressBackend())

    path: str | None = Field(default=None)

    path_type: str | None = Field(
        default=None,
        serialization_alias="pathType",
        validation_alias=AliasChoices("path_type", "pathType"),
    )

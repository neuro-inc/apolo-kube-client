from pydantic import AliasChoices, BaseModel, Field
from .base import _default_if_none
from .v1_ingress_backend import V1IngressBackend
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1HTTPIngressPath",)


class V1HTTPIngressPath(BaseModel):
    backend: Annotated[
        V1IngressBackend, BeforeValidator(_default_if_none(V1IngressBackend))
    ] = Field(default_factory=lambda: V1IngressBackend())

    path: str | None = None

    path_type: str | None = Field(
        default=None,
        serialization_alias="pathType",
        validation_alias=AliasChoices("path_type", "pathType"),
    )

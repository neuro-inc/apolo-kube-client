from pydantic import AliasChoices, BaseModel, Field
from .utils import _default_if_none
from .utils import _exclude_if
from .v1_ingress_backend import V1IngressBackend
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1HTTPIngressPath",)


class V1HTTPIngressPath(BaseModel):
    backend: Annotated[
        V1IngressBackend, BeforeValidator(_default_if_none(V1IngressBackend))
    ] = Field(default_factory=lambda: V1IngressBackend(), exclude_if=_exclude_if)

    path: str | None = Field(default=None, exclude_if=_exclude_if)

    path_type: str | None = Field(
        default=None,
        serialization_alias="pathType",
        validation_alias=AliasChoices("path_type", "pathType"),
        exclude_if=_exclude_if,
    )

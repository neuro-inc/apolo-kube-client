from pydantic import BaseModel, Field
from .utils import _default_if_none
from .utils import _exclude_if
from .v1_ingress_class_parameters_reference import V1IngressClassParametersReference
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1IngressClassSpec",)


class V1IngressClassSpec(BaseModel):
    controller: str | None = Field(default=None, exclude_if=_exclude_if)

    parameters: Annotated[
        V1IngressClassParametersReference,
        BeforeValidator(_default_if_none(V1IngressClassParametersReference)),
    ] = Field(
        default_factory=lambda: V1IngressClassParametersReference(),
        exclude_if=_exclude_if,
    )

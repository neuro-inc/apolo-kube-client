from pydantic import BaseModel, Field
from .utils import _default_if_none
from .v1_ingress_class_parameters_reference import V1IngressClassParametersReference
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1IngressClassSpec",)


class V1IngressClassSpec(BaseModel):
    controller: str | None = None

    parameters: Annotated[
        V1IngressClassParametersReference,
        BeforeValidator(_default_if_none(V1IngressClassParametersReference)),
    ] = Field(default_factory=lambda: V1IngressClassParametersReference())

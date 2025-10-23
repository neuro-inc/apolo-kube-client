from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _default_if_none
from .v1_ingress_class_parameters_reference import V1IngressClassParametersReference
from pydantic import BeforeValidator

__all__ = ("V1IngressClassSpec",)


class V1IngressClassSpec(BaseModel):
    """IngressClassSpec provides information about the class of an Ingress."""

    model_config = ConfigDict(validate_by_alias=True, validate_by_name=True)

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.networking.v1.IngressClassSpec"

    controller: Annotated[
        str | None,
        Field(
            description="""controller refers to the name of the controller that should handle this class. This allows for different "flavors" that are controlled by the same controller. For example, you may have different parameters for the same implementing controller. This should be specified as a domain-prefixed path no more than 250 characters in length, e.g. "acme.io/ingress-controller". This field is immutable.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    parameters: Annotated[
        V1IngressClassParametersReference | None,
        Field(
            description="""parameters is a link to a custom resource containing additional configuration for the controller. This is optional if the controller does not require extra parameters.""",
            exclude_if=lambda v: v is None,
        ),
        BeforeValidator(_default_if_none(V1IngressClassParametersReference)),
    ] = None

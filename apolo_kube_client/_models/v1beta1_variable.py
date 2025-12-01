from typing import Annotated, ClassVar, Final

from pydantic import Field

from .base_model import BaseConfiguredModel


__all__ = ("V1beta1Variable",)


class V1beta1Variable(BaseConfiguredModel):
    """Variable is the definition of a variable that is used for composition. A variable is defined as a named expression."""

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.admissionregistration.v1beta1.Variable"
    )

    expression: Annotated[
        str,
        Field(
            description="""Expression is the expression that will be evaluated as the value of the variable. The CEL expression has access to the same identifiers as the CEL expressions in Validation."""
        ),
    ]

    name: Annotated[
        str,
        Field(
            description="""Name is the name of the variable. The name must be a valid CEL identifier and unique among all variables. The variable can be accessed in other expressions through `variables` For example, if name is "foo", the variable will be available as `variables.foo`"""
        ),
    ]

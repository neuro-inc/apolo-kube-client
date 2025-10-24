from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("V1alpha1Variable",)


class V1alpha1Variable(BaseModel):
    """Variable is the definition of a variable that is used for composition."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.admissionregistration.v1alpha1.Variable"
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

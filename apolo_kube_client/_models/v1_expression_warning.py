from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("V1ExpressionWarning",)


class V1ExpressionWarning(BaseModel):
    """ExpressionWarning is a warning information that targets a specific expression."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.admissionregistration.v1.ExpressionWarning"
    )

    field_ref: Annotated[
        str,
        Field(
            alias="fieldRef",
            description='''The path to the field that refers the expression. For example, the reference to the expression of the first item of validations is "spec.validations[0].expression"''',
        ),
    ]

    warning: Annotated[
        str,
        Field(
            description="""The content of type checking information in a human-readable form. Each line of the warning contains the type that the expression is checked against, followed by the type check error from the compiler."""
        ),
    ]

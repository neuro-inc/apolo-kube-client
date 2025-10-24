from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _collection_if_none
from .v1_expression_warning import V1ExpressionWarning
from pydantic import BeforeValidator

__all__ = ("V1TypeChecking",)


class V1TypeChecking(BaseModel):
    """TypeChecking contains results of type checking the expressions in the ValidatingAdmissionPolicy"""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.admissionregistration.v1.TypeChecking"
    )

    expression_warnings: Annotated[
        list[V1ExpressionWarning],
        Field(
            alias="expressionWarnings",
            description="""The type checking warnings for each expression.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

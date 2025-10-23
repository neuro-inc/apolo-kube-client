from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .utils import _exclude_if
from .v1_expression_warning import V1ExpressionWarning
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1TypeChecking",)


class V1TypeChecking(BaseModel):
    expression_warnings: Annotated[
        list[V1ExpressionWarning], BeforeValidator(_collection_if_none("[]"))
    ] = Field(
        default=[],
        serialization_alias="expressionWarnings",
        validation_alias=AliasChoices("expression_warnings", "expressionWarnings"),
        exclude_if=_exclude_if,
    )

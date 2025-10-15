from pydantic import BaseModel, Field

from .v1beta1_expression_warning import V1beta1ExpressionWarning


class V1beta1TypeChecking(BaseModel):
    expression_warnings: list[V1beta1ExpressionWarning] | None = Field(
        None, alias="expressionWarnings"
    )

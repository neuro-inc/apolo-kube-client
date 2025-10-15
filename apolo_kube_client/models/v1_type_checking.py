from pydantic import BaseModel, Field

from .v1_expression_warning import V1ExpressionWarning


class V1TypeChecking(BaseModel):
    expression_warnings: list[V1ExpressionWarning] | None = Field(
        None, alias="expressionWarnings"
    )

from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_expression_warning import V1ExpressionWarning

__all__ = ("V1TypeChecking",)


class V1TypeChecking(BaseModel):
    expression_warnings: list[V1ExpressionWarning] = Field(
        default_factory=lambda: [], alias="expressionWarnings"
    )

from __future__ import annotations

from pydantic import BaseModel, Field

from .v1beta1_expression_warning import V1beta1ExpressionWarning

__all__ = ("V1beta1TypeChecking",)


class V1beta1TypeChecking(BaseModel):
    expression_warnings: list[V1beta1ExpressionWarning] | None = Field(
        None, alias="expressionWarnings"
    )

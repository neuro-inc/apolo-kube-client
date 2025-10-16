from __future__ import annotations

from pydantic import BaseModel, Field

__all__ = ("V1beta1ExpressionWarning",)


class V1beta1ExpressionWarning(BaseModel):
    field_ref: str | None = Field(None, alias="fieldRef")

    warning: str | None = Field(None, alias="warning")

from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1ExpressionWarning",)


class V1ExpressionWarning(BaseModel):
    field_ref: str | None = Field(default_factory=lambda: None, alias="fieldRef")

    warning: str | None = Field(default_factory=lambda: None)

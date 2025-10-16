from __future__ import annotations

from pydantic import BaseModel, Field

__all__ = ("V1AuditAnnotation",)


class V1AuditAnnotation(BaseModel):
    key: str | None = Field(None, alias="key")

    value_expression: str | None = Field(None, alias="valueExpression")

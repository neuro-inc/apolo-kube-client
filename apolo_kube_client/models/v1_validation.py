from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1Validation",)


class V1Validation(BaseModel):
    expression: str | None = Field(default_factory=lambda: None)

    message: str | None = Field(default_factory=lambda: None)

    message_expression: str | None = Field(
        default_factory=lambda: None, alias="messageExpression"
    )

    reason: str | None = Field(default_factory=lambda: None)

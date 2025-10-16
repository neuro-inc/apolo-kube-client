from __future__ import annotations

from pydantic import BaseModel, Field

__all__ = ("V1beta1Validation",)


class V1beta1Validation(BaseModel):
    expression: str | None = Field(None, alias="expression")

    message: str | None = Field(None, alias="message")

    message_expression: str | None = Field(None, alias="messageExpression")

    reason: str | None = Field(None, alias="reason")

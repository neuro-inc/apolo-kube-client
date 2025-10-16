from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1ValidationRule",)


class V1ValidationRule(BaseModel):
    field_path: str | None = Field(default_factory=lambda: None, alias="fieldPath")

    message: str | None = Field(default_factory=lambda: None, alias="message")

    message_expression: str | None = Field(
        default_factory=lambda: None, alias="messageExpression"
    )

    optional_old_self: bool | None = Field(
        default_factory=lambda: None, alias="optionalOldSelf"
    )

    reason: str | None = Field(default_factory=lambda: None, alias="reason")

    rule: str | None = Field(default_factory=lambda: None, alias="rule")

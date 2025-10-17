from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field


__all__ = ("V1Validation",)


class V1Validation(BaseModel):
    expression: str | None = Field(default=None)

    message: str | None = Field(default=None)

    message_expression: str | None = Field(
        default=None,
        serialization_alias="messageExpression",
        validation_alias=AliasChoices("message_expression", "messageExpression"),
    )

    reason: str | None = Field(default=None)

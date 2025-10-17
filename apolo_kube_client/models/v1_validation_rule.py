from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field


__all__ = ("V1ValidationRule",)


class V1ValidationRule(BaseModel):
    field_path: str | None = Field(
        default=None,
        serialization_alias="fieldPath",
        validation_alias=AliasChoices("field_path", "fieldPath"),
    )

    message: str | None = Field(default=None)

    message_expression: str | None = Field(
        default=None,
        serialization_alias="messageExpression",
        validation_alias=AliasChoices("message_expression", "messageExpression"),
    )

    optional_old_self: bool | None = Field(
        default=None,
        serialization_alias="optionalOldSelf",
        validation_alias=AliasChoices("optional_old_self", "optionalOldSelf"),
    )

    reason: str | None = Field(default=None)

    rule: str | None = Field(default=None)

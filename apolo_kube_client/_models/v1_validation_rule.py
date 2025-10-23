from pydantic import AliasChoices, BaseModel, Field
from .utils import _exclude_if

__all__ = ("V1ValidationRule",)


class V1ValidationRule(BaseModel):
    field_path: str | None = Field(
        default=None,
        serialization_alias="fieldPath",
        validation_alias=AliasChoices("field_path", "fieldPath"),
        exclude_if=_exclude_if,
    )

    message: str | None = Field(default=None, exclude_if=_exclude_if)

    message_expression: str | None = Field(
        default=None,
        serialization_alias="messageExpression",
        validation_alias=AliasChoices("message_expression", "messageExpression"),
        exclude_if=_exclude_if,
    )

    optional_old_self: bool | None = Field(
        default=None,
        serialization_alias="optionalOldSelf",
        validation_alias=AliasChoices("optional_old_self", "optionalOldSelf"),
        exclude_if=_exclude_if,
    )

    reason: str | None = Field(default=None, exclude_if=_exclude_if)

    rule: str | None = Field(default=None, exclude_if=_exclude_if)

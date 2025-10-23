from pydantic import AliasChoices, BaseModel, Field
from .utils import _exclude_if

__all__ = ("V1Validation",)


class V1Validation(BaseModel):
    expression: str | None = Field(default=None, exclude_if=_exclude_if)

    message: str | None = Field(default=None, exclude_if=_exclude_if)

    message_expression: str | None = Field(
        default=None,
        serialization_alias="messageExpression",
        validation_alias=AliasChoices("message_expression", "messageExpression"),
        exclude_if=_exclude_if,
    )

    reason: str | None = Field(default=None, exclude_if=_exclude_if)

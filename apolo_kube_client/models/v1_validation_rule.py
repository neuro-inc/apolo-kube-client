from pydantic import BaseModel, Field


class V1ValidationRule(BaseModel):
    field_path: str | None = Field(None, alias="fieldPath")

    message: str | None = Field(None, alias="message")

    message_expression: str | None = Field(None, alias="messageExpression")

    optional_old_self: bool | None = Field(None, alias="optionalOldSelf")

    reason: str | None = Field(None, alias="reason")

    rule: str | None = Field(None, alias="rule")

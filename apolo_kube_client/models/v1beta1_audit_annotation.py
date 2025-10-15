from pydantic import BaseModel, Field


class V1beta1AuditAnnotation(BaseModel):
    key: str | None = Field(None, alias="key")

    value_expression: str | None = Field(None, alias="valueExpression")

from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field


__all__ = ("V1AuditAnnotation",)


class V1AuditAnnotation(BaseModel):
    key: str | None = Field(default=None)

    value_expression: str | None = Field(
        default=None,
        serialization_alias="valueExpression",
        validation_alias=AliasChoices("value_expression", "valueExpression"),
    )

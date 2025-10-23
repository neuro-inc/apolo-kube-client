from pydantic import AliasChoices, BaseModel, Field
from .utils import _exclude_if

__all__ = ("V1AuditAnnotation",)


class V1AuditAnnotation(BaseModel):
    key: str | None = Field(default=None, exclude_if=_exclude_if)

    value_expression: str | None = Field(
        default=None,
        serialization_alias="valueExpression",
        validation_alias=AliasChoices("value_expression", "valueExpression"),
        exclude_if=_exclude_if,
    )

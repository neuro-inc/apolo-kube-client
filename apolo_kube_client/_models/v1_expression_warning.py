from pydantic import AliasChoices, BaseModel, Field
from .utils import _exclude_if

__all__ = ("V1ExpressionWarning",)


class V1ExpressionWarning(BaseModel):
    field_ref: str | None = Field(
        default=None,
        serialization_alias="fieldRef",
        validation_alias=AliasChoices("field_ref", "fieldRef"),
        exclude_if=_exclude_if,
    )

    warning: str | None = Field(default=None, exclude_if=_exclude_if)

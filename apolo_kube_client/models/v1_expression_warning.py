from pydantic import AliasChoices, BaseModel, Field


__all__ = ("V1ExpressionWarning",)


class V1ExpressionWarning(BaseModel):
    field_ref: str | None = Field(
        default=None,
        serialization_alias="fieldRef",
        validation_alias=AliasChoices("field_ref", "fieldRef"),
    )

    warning: str | None = None

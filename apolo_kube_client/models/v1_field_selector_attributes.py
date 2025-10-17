from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_field_selector_requirement import V1FieldSelectorRequirement

__all__ = ("V1FieldSelectorAttributes",)


class V1FieldSelectorAttributes(BaseModel):
    raw_selector: str | None = Field(
        default=None,
        serialization_alias="rawSelector",
        validation_alias=AliasChoices("raw_selector", "rawSelector"),
    )

    requirements: list[V1FieldSelectorRequirement] = Field(default=[])

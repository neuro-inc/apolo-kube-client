from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_field_selector_requirement import V1FieldSelectorRequirement

__all__ = ("V1FieldSelectorAttributes",)


class V1FieldSelectorAttributes(BaseModel):
    raw_selector: str | None = Field(default_factory=lambda: None, alias="rawSelector")

    requirements: list[V1FieldSelectorRequirement] = Field(
        default_factory=lambda: [], alias="requirements"
    )

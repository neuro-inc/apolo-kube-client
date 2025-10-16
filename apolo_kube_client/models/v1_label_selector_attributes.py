from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_label_selector_requirement import V1LabelSelectorRequirement

__all__ = ("V1LabelSelectorAttributes",)


class V1LabelSelectorAttributes(BaseModel):
    raw_selector: str | None = Field(default_factory=lambda: None, alias="rawSelector")

    requirements: list[V1LabelSelectorRequirement] = Field(
        default_factory=lambda: [], alias="requirements"
    )

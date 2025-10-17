from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_label_selector_requirement import V1LabelSelectorRequirement

__all__ = ("V1LabelSelector",)


class V1LabelSelector(BaseModel):
    match_expressions: list[V1LabelSelectorRequirement] = Field(
        default_factory=lambda: [], alias="matchExpressions"
    )

    match_labels: dict[str, str] = Field(
        default_factory=lambda: {}, alias="matchLabels"
    )

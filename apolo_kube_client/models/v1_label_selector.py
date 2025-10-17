from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_label_selector_requirement import V1LabelSelectorRequirement

__all__ = ("V1LabelSelector",)


class V1LabelSelector(BaseModel):
    match_expressions: list[V1LabelSelectorRequirement] = Field(
        default=[],
        serialization_alias="matchExpressions",
        validation_alias=AliasChoices("match_expressions", "matchExpressions"),
    )

    match_labels: dict[str, str] = Field(
        default={},
        serialization_alias="matchLabels",
        validation_alias=AliasChoices("match_labels", "matchLabels"),
    )

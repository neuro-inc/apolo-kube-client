from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_node_selector_requirement import V1NodeSelectorRequirement

__all__ = ("V1NodeSelectorTerm",)


class V1NodeSelectorTerm(BaseModel):
    match_expressions: list[V1NodeSelectorRequirement] = Field(
        default_factory=lambda: [], alias="matchExpressions"
    )

    match_fields: list[V1NodeSelectorRequirement] = Field(
        default_factory=lambda: [], alias="matchFields"
    )

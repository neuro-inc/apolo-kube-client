from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_topology_selector_label_requirement import V1TopologySelectorLabelRequirement

__all__ = ("V1TopologySelectorTerm",)


class V1TopologySelectorTerm(BaseModel):
    match_label_expressions: list[V1TopologySelectorLabelRequirement] = Field(
        default_factory=lambda: [], alias="matchLabelExpressions"
    )

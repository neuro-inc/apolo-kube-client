from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_topology_selector_label_requirement import V1TopologySelectorLabelRequirement

__all__ = ("V1TopologySelectorTerm",)


class V1TopologySelectorTerm(BaseModel):
    match_label_expressions: list[V1TopologySelectorLabelRequirement] = Field(
        default=[],
        serialization_alias="matchLabelExpressions",
        validation_alias=AliasChoices(
            "match_label_expressions", "matchLabelExpressions"
        ),
    )

from pydantic import AliasChoices, BaseModel, Field
from .v1_node_selector_requirement import V1NodeSelectorRequirement

__all__ = ("V1NodeSelectorTerm",)


class V1NodeSelectorTerm(BaseModel):
    match_expressions: list[V1NodeSelectorRequirement] = Field(
        default=[],
        serialization_alias="matchExpressions",
        validation_alias=AliasChoices("match_expressions", "matchExpressions"),
    )

    match_fields: list[V1NodeSelectorRequirement] = Field(
        default=[],
        serialization_alias="matchFields",
        validation_alias=AliasChoices("match_fields", "matchFields"),
    )

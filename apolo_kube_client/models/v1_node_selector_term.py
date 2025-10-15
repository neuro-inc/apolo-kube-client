from pydantic import BaseModel, Field

from .v1_node_selector_requirement import V1NodeSelectorRequirement


class V1NodeSelectorTerm(BaseModel):
    match_expressions: list[V1NodeSelectorRequirement] | None = Field(
        None, alias="matchExpressions"
    )

    match_fields: list[V1NodeSelectorRequirement] | None = Field(
        None, alias="matchFields"
    )

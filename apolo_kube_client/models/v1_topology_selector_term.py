from pydantic import BaseModel, Field

from .v1_topology_selector_label_requirement import V1TopologySelectorLabelRequirement


class V1TopologySelectorTerm(BaseModel):
    match_label_expressions: list[V1TopologySelectorLabelRequirement] | None = Field(
        None, alias="matchLabelExpressions"
    )

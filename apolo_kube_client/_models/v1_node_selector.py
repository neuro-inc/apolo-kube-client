from pydantic import AliasChoices, BaseModel, Field
from .v1_node_selector_term import V1NodeSelectorTerm

__all__ = ("V1NodeSelector",)


class V1NodeSelector(BaseModel):
    node_selector_terms: list[V1NodeSelectorTerm] = Field(
        default=[],
        serialization_alias="nodeSelectorTerms",
        validation_alias=AliasChoices("node_selector_terms", "nodeSelectorTerms"),
    )

from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .v1_node_selector_requirement import V1NodeSelectorRequirement
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1NodeSelectorTerm",)


class V1NodeSelectorTerm(BaseModel):
    match_expressions: Annotated[
        list[V1NodeSelectorRequirement], BeforeValidator(_collection_if_none("[]"))
    ] = Field(
        default=[],
        serialization_alias="matchExpressions",
        validation_alias=AliasChoices("match_expressions", "matchExpressions"),
    )

    match_fields: Annotated[
        list[V1NodeSelectorRequirement], BeforeValidator(_collection_if_none("[]"))
    ] = Field(
        default=[],
        serialization_alias="matchFields",
        validation_alias=AliasChoices("match_fields", "matchFields"),
    )

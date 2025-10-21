from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .v1_node_selector_term import V1NodeSelectorTerm
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1NodeSelector",)


class V1NodeSelector(BaseModel):
    node_selector_terms: Annotated[
        list[V1NodeSelectorTerm], BeforeValidator(_collection_if_none("[]"))
    ] = Field(
        default=[],
        serialization_alias="nodeSelectorTerms",
        validation_alias=AliasChoices("node_selector_terms", "nodeSelectorTerms"),
    )

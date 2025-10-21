from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .v1_topology_selector_label_requirement import V1TopologySelectorLabelRequirement
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1TopologySelectorTerm",)


class V1TopologySelectorTerm(BaseModel):
    match_label_expressions: Annotated[
        list[V1TopologySelectorLabelRequirement],
        BeforeValidator(_collection_if_none("[]")),
    ] = Field(
        default=[],
        serialization_alias="matchLabelExpressions",
        validation_alias=AliasChoices(
            "match_label_expressions", "matchLabelExpressions"
        ),
    )

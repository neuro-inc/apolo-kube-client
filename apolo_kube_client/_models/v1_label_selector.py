from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .v1_label_selector_requirement import V1LabelSelectorRequirement
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1LabelSelector",)


class V1LabelSelector(BaseModel):
    match_expressions: Annotated[
        list[V1LabelSelectorRequirement], BeforeValidator(_collection_if_none("[]"))
    ] = Field(
        default=[],
        serialization_alias="matchExpressions",
        validation_alias=AliasChoices("match_expressions", "matchExpressions"),
    )

    match_labels: Annotated[
        dict[str, str], BeforeValidator(_collection_if_none("{}"))
    ] = Field(
        default={},
        serialization_alias="matchLabels",
        validation_alias=AliasChoices("match_labels", "matchLabels"),
    )

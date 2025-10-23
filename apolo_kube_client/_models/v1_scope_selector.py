from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .utils import _exclude_if
from .v1_scoped_resource_selector_requirement import V1ScopedResourceSelectorRequirement
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1ScopeSelector",)


class V1ScopeSelector(BaseModel):
    match_expressions: Annotated[
        list[V1ScopedResourceSelectorRequirement],
        BeforeValidator(_collection_if_none("[]")),
    ] = Field(
        default=[],
        serialization_alias="matchExpressions",
        validation_alias=AliasChoices("match_expressions", "matchExpressions"),
        exclude_if=_exclude_if,
    )

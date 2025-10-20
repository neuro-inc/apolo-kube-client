from pydantic import AliasChoices, BaseModel, Field
from .v1_scoped_resource_selector_requirement import V1ScopedResourceSelectorRequirement

__all__ = ("V1ScopeSelector",)


class V1ScopeSelector(BaseModel):
    match_expressions: list[V1ScopedResourceSelectorRequirement] = Field(
        default=[],
        serialization_alias="matchExpressions",
        validation_alias=AliasChoices("match_expressions", "matchExpressions"),
    )

from pydantic import BaseModel, Field

from .v1_scoped_resource_selector_requirement import V1ScopedResourceSelectorRequirement


class V1ScopeSelector(BaseModel):
    match_expressions: list[V1ScopedResourceSelectorRequirement] | None = Field(
        None, alias="matchExpressions"
    )

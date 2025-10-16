from __future__ import annotations

from pydantic import BaseModel, Field

from .v1_scoped_resource_selector_requirement import V1ScopedResourceSelectorRequirement

__all__ = ("V1ScopeSelector",)


class V1ScopeSelector(BaseModel):
    match_expressions: list[V1ScopedResourceSelectorRequirement] | None = Field(
        None, alias="matchExpressions"
    )

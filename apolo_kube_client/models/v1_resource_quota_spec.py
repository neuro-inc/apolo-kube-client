from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_scope_selector import V1ScopeSelector

__all__ = ("V1ResourceQuotaSpec",)


class V1ResourceQuotaSpec(BaseModel):
    hard: dict[str, str] = Field(default={})

    scope_selector: V1ScopeSelector = Field(
        default_factory=lambda: V1ScopeSelector(),
        serialization_alias="scopeSelector",
        validation_alias=AliasChoices("scope_selector", "scopeSelector"),
    )

    scopes: list[str] = Field(default=[])

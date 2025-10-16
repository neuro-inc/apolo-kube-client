from __future__ import annotations

from pydantic import BaseModel, Field

from .v1_scope_selector import V1ScopeSelector

__all__ = ("V1ResourceQuotaSpec",)


class V1ResourceQuotaSpec(BaseModel):
    hard: dict[str, str] | None = Field(None, alias="hard")

    scope_selector: V1ScopeSelector | None = Field(None, alias="scopeSelector")

    scopes: list[str] | None = Field(None, alias="scopes")

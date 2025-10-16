from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1ScopedResourceSelectorRequirement",)


class V1ScopedResourceSelectorRequirement(BaseModel):
    operator: str | None = Field(default_factory=lambda: None, alias="operator")

    scope_name: str | None = Field(default_factory=lambda: None, alias="scopeName")

    values: list[str] = Field(default_factory=lambda: [], alias="values")

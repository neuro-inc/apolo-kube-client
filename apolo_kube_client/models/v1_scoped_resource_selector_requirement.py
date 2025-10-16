from __future__ import annotations

from pydantic import BaseModel, Field

__all__ = ("V1ScopedResourceSelectorRequirement",)


class V1ScopedResourceSelectorRequirement(BaseModel):
    operator: str | None = Field(None, alias="operator")

    scope_name: str | None = Field(None, alias="scopeName")

    values: list[str] | None = Field(None, alias="values")

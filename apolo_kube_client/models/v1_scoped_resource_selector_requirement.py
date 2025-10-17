from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field


__all__ = ("V1ScopedResourceSelectorRequirement",)


class V1ScopedResourceSelectorRequirement(BaseModel):
    operator: str | None = Field(default=None)

    scope_name: str | None = Field(
        default=None,
        serialization_alias="scopeName",
        validation_alias=AliasChoices("scope_name", "scopeName"),
    )

    values: list[str] = Field(default=[])

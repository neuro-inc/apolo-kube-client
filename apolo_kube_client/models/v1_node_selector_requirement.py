from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1NodeSelectorRequirement",)


class V1NodeSelectorRequirement(BaseModel):
    key: str | None = Field(default_factory=lambda: None, alias="key")

    operator: str | None = Field(default_factory=lambda: None, alias="operator")

    values: list[str] = Field(default_factory=lambda: [], alias="values")

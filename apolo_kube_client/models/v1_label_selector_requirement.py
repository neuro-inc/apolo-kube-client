from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1LabelSelectorRequirement",)


class V1LabelSelectorRequirement(BaseModel):
    key: str | None = Field(default_factory=lambda: None, alias="key")

    operator: str | None = Field(default_factory=lambda: None, alias="operator")

    values: list[str] = Field(default_factory=lambda: [], alias="values")

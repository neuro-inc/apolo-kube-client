from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1NodeSelectorRequirement",)


class V1NodeSelectorRequirement(BaseModel):
    key: str | None = Field(default_factory=lambda: None)

    operator: str | None = Field(default_factory=lambda: None)

    values: list[str] = Field(default_factory=lambda: [])

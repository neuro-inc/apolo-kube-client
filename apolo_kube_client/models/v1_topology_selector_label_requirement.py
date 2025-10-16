from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1TopologySelectorLabelRequirement",)


class V1TopologySelectorLabelRequirement(BaseModel):
    key: str | None = Field(default_factory=lambda: None, alias="key")

    values: list[str] = Field(default_factory=lambda: [], alias="values")

from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1LabelSelectorRequirement",)


class V1LabelSelectorRequirement(BaseModel):
    key: str | None = Field(default=None)

    operator: str | None = Field(default=None)

    values: list[str] = Field(default=[])

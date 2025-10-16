from __future__ import annotations

from pydantic import BaseModel, Field

__all__ = ("V1LabelSelectorRequirement",)


class V1LabelSelectorRequirement(BaseModel):
    key: str | None = Field(None, alias="key")

    operator: str | None = Field(None, alias="operator")

    values: list[str] | None = Field(None, alias="values")

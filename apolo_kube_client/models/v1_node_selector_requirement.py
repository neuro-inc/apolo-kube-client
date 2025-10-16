from __future__ import annotations

from pydantic import BaseModel, Field

__all__ = ("V1NodeSelectorRequirement",)


class V1NodeSelectorRequirement(BaseModel):
    key: str | None = Field(None, alias="key")

    operator: str | None = Field(None, alias="operator")

    values: list[str] | None = Field(None, alias="values")

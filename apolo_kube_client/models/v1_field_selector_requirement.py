from __future__ import annotations

from pydantic import BaseModel, Field

__all__ = ("V1FieldSelectorRequirement",)


class V1FieldSelectorRequirement(BaseModel):
    key: str | None = Field(None, alias="key")

    operator: str | None = Field(None, alias="operator")

    values: list[str] | None = Field(None, alias="values")

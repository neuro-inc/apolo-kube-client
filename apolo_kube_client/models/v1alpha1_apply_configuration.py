from __future__ import annotations

from pydantic import BaseModel, Field

__all__ = ("V1alpha1ApplyConfiguration",)


class V1alpha1ApplyConfiguration(BaseModel):
    expression: str | None = Field(None, alias="expression")

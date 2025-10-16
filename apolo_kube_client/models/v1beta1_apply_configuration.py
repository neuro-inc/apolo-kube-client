from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1beta1ApplyConfiguration",)


class V1beta1ApplyConfiguration(BaseModel):
    expression: str | None = Field(default_factory=lambda: None, alias="expression")

from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1beta1JSONPatch",)


class V1beta1JSONPatch(BaseModel):
    expression: str | None = Field(default_factory=lambda: None, alias="expression")

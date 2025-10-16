from __future__ import annotations

from pydantic import BaseModel, Field

__all__ = ("V1alpha1JSONPatch",)


class V1alpha1JSONPatch(BaseModel):
    expression: str | None = Field(None, alias="expression")

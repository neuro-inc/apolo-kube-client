from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1alpha1Variable",)


class V1alpha1Variable(BaseModel):
    expression: str | None = Field(default_factory=lambda: None)

    name: str | None = Field(default_factory=lambda: None)

from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1Variable",)


class V1Variable(BaseModel):
    expression: str | None = Field(default_factory=lambda: None, alias="expression")

    name: str | None = Field(default_factory=lambda: None, alias="name")

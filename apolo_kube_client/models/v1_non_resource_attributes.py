from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1NonResourceAttributes",)


class V1NonResourceAttributes(BaseModel):
    path: str | None = Field(default_factory=lambda: None, alias="path")

    verb: str | None = Field(default_factory=lambda: None, alias="verb")

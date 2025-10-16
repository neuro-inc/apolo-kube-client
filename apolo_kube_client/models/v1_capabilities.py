from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1Capabilities",)


class V1Capabilities(BaseModel):
    add: list[str] = Field(default_factory=lambda: [], alias="add")

    drop: list[str] = Field(default_factory=lambda: [], alias="drop")

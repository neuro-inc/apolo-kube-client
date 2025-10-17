from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1LocalObjectReference",)


class V1LocalObjectReference(BaseModel):
    name: str | None = Field(default=None)

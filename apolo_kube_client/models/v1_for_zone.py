from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1ForZone",)


class V1ForZone(BaseModel):
    name: str | None = Field(default_factory=lambda: None, alias="name")

from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1PodOS",)


class V1PodOS(BaseModel):
    name: str | None = Field(default_factory=lambda: None)

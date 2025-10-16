from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1VolumeNodeResources",)


class V1VolumeNodeResources(BaseModel):
    count: int | None = Field(default_factory=lambda: None, alias="count")

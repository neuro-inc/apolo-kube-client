from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1PriorityLevelConfigurationReference",)


class V1PriorityLevelConfigurationReference(BaseModel):
    name: str | None = Field(default_factory=lambda: None)

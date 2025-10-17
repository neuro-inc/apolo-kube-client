from __future__ import annotations
from pydantic import BaseModel, Field
from datetime import datetime

__all__ = ("V1ContainerStateRunning",)


class V1ContainerStateRunning(BaseModel):
    started_at: datetime | None = Field(default_factory=lambda: None, alias="startedAt")

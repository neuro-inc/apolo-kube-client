from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field

__all__ = ("V1ContainerStateRunning",)


class V1ContainerStateRunning(BaseModel):
    started_at: datetime | None = Field(None, alias="startedAt")

from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from datetime import datetime

__all__ = ("V1ContainerStateRunning",)


class V1ContainerStateRunning(BaseModel):
    started_at: datetime | None = Field(
        default=None,
        serialization_alias="startedAt",
        validation_alias=AliasChoices("started_at", "startedAt"),
    )

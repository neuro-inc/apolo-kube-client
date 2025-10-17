from __future__ import annotations
from pydantic import BaseModel, Field
from datetime import datetime

__all__ = ("V1ContainerStateTerminated",)


class V1ContainerStateTerminated(BaseModel):
    container_id: str | None = Field(default_factory=lambda: None, alias="containerID")

    exit_code: int | None = Field(default_factory=lambda: None, alias="exitCode")

    finished_at: datetime | None = Field(
        default_factory=lambda: None, alias="finishedAt"
    )

    message: str | None = Field(default_factory=lambda: None)

    reason: str | None = Field(default_factory=lambda: None)

    signal: int | None = Field(default_factory=lambda: None)

    started_at: datetime | None = Field(default_factory=lambda: None, alias="startedAt")

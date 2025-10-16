from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field

__all__ = ("V1ContainerStateTerminated",)


class V1ContainerStateTerminated(BaseModel):
    container_id: str | None = Field(None, alias="containerID")

    exit_code: int | None = Field(None, alias="exitCode")

    finished_at: datetime | None = Field(None, alias="finishedAt")

    message: str | None = Field(None, alias="message")

    reason: str | None = Field(None, alias="reason")

    signal: int | None = Field(None, alias="signal")

    started_at: datetime | None = Field(None, alias="startedAt")

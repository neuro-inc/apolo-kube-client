from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from datetime import datetime

__all__ = ("V1ContainerStateTerminated",)


class V1ContainerStateTerminated(BaseModel):
    container_id: str | None = Field(
        default=None,
        serialization_alias="containerID",
        validation_alias=AliasChoices("container_id", "containerID"),
    )

    exit_code: int | None = Field(
        default=None,
        serialization_alias="exitCode",
        validation_alias=AliasChoices("exit_code", "exitCode"),
    )

    finished_at: datetime | None = Field(
        default=None,
        serialization_alias="finishedAt",
        validation_alias=AliasChoices("finished_at", "finishedAt"),
    )

    message: str | None = Field(default=None)

    reason: str | None = Field(default=None)

    signal: int | None = Field(default=None)

    started_at: datetime | None = Field(
        default=None,
        serialization_alias="startedAt",
        validation_alias=AliasChoices("started_at", "startedAt"),
    )

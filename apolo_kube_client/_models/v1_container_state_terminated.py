from pydantic import AliasChoices, BaseModel, Field
from .utils import _exclude_if
from datetime import datetime

__all__ = ("V1ContainerStateTerminated",)


class V1ContainerStateTerminated(BaseModel):
    container_id: str | None = Field(
        default=None,
        serialization_alias="containerID",
        validation_alias=AliasChoices("container_id", "containerID"),
        exclude_if=_exclude_if,
    )

    exit_code: int | None = Field(
        default=None,
        serialization_alias="exitCode",
        validation_alias=AliasChoices("exit_code", "exitCode"),
        exclude_if=_exclude_if,
    )

    finished_at: datetime | None = Field(
        default=None,
        serialization_alias="finishedAt",
        validation_alias=AliasChoices("finished_at", "finishedAt"),
        exclude_if=_exclude_if,
    )

    message: str | None = Field(default=None, exclude_if=_exclude_if)

    reason: str | None = Field(default=None, exclude_if=_exclude_if)

    signal: int | None = Field(default=None, exclude_if=_exclude_if)

    started_at: datetime | None = Field(
        default=None,
        serialization_alias="startedAt",
        validation_alias=AliasChoices("started_at", "startedAt"),
        exclude_if=_exclude_if,
    )

from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_object_reference import V1ObjectReference
from datetime import datetime

__all__ = ("V1CronJobStatus",)


class V1CronJobStatus(BaseModel):
    active: list[V1ObjectReference] = Field(default=[])

    last_schedule_time: datetime | None = Field(
        default=None,
        serialization_alias="lastScheduleTime",
        validation_alias=AliasChoices("last_schedule_time", "lastScheduleTime"),
    )

    last_successful_time: datetime | None = Field(
        default=None,
        serialization_alias="lastSuccessfulTime",
        validation_alias=AliasChoices("last_successful_time", "lastSuccessfulTime"),
    )

from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_object_reference import V1ObjectReference
from datetime import datetime

__all__ = ("V1CronJobStatus",)


class V1CronJobStatus(BaseModel):
    active: list[V1ObjectReference] = Field(default_factory=lambda: [])

    last_schedule_time: datetime | None = Field(
        default_factory=lambda: None, alias="lastScheduleTime"
    )

    last_successful_time: datetime | None = Field(
        default_factory=lambda: None, alias="lastSuccessfulTime"
    )

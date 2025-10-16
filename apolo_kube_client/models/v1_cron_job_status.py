from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field

from .v1_object_reference import V1ObjectReference

__all__ = ("V1CronJobStatus",)


class V1CronJobStatus(BaseModel):
    active: list[V1ObjectReference] | None = Field(None, alias="active")

    last_schedule_time: datetime | None = Field(None, alias="lastScheduleTime")

    last_successful_time: datetime | None = Field(None, alias="lastSuccessfulTime")

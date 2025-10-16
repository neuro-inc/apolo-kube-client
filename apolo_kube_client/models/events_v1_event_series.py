from __future__ import annotations
from pydantic import BaseModel, Field
from datetime import datetime

__all__ = ("EventsV1EventSeries",)


class EventsV1EventSeries(BaseModel):
    count: int | None = Field(default_factory=lambda: None, alias="count")

    last_observed_time: datetime | None = Field(
        default_factory=lambda: None, alias="lastObservedTime"
    )

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field

__all__ = ("EventsV1EventSeries",)


class EventsV1EventSeries(BaseModel):
    count: int | None = Field(None, alias="count")

    last_observed_time: datetime | None = Field(None, alias="lastObservedTime")

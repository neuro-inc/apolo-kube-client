from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field

__all__ = ("CoreV1EventSeries",)


class CoreV1EventSeries(BaseModel):
    count: int | None = Field(None, alias="count")

    last_observed_time: datetime | None = Field(None, alias="lastObservedTime")

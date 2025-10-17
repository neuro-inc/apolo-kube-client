from __future__ import annotations
from pydantic import BaseModel, Field
from datetime import datetime

__all__ = ("CoreV1EventSeries",)


class CoreV1EventSeries(BaseModel):
    count: int | None = Field(default_factory=lambda: None)

    last_observed_time: datetime | None = Field(
        default_factory=lambda: None, alias="lastObservedTime"
    )

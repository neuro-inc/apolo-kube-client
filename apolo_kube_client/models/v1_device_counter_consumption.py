from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_counter import V1Counter

__all__ = ("V1DeviceCounterConsumption",)


class V1DeviceCounterConsumption(BaseModel):
    counter_set: str | None = Field(default_factory=lambda: None, alias="counterSet")

    counters: dict[str, V1Counter] = Field(default_factory=lambda: {}, alias="counters")

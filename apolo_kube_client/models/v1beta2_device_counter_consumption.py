from __future__ import annotations
from pydantic import BaseModel, Field
from .v1beta2_counter import V1beta2Counter

__all__ = ("V1beta2DeviceCounterConsumption",)


class V1beta2DeviceCounterConsumption(BaseModel):
    counter_set: str | None = Field(default_factory=lambda: None, alias="counterSet")

    counters: dict[str, V1beta2Counter] = Field(default_factory=lambda: {})

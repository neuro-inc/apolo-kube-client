from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1beta2_counter import V1beta2Counter

__all__ = ("V1beta2DeviceCounterConsumption",)


class V1beta2DeviceCounterConsumption(BaseModel):
    counter_set: str | None = Field(
        default=None,
        serialization_alias="counterSet",
        validation_alias=AliasChoices("counter_set", "counterSet"),
    )

    counters: dict[str, V1beta2Counter] = Field(default={})

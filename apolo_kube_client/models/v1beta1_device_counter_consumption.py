from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1beta1_counter import V1beta1Counter

__all__ = ("V1beta1DeviceCounterConsumption",)


class V1beta1DeviceCounterConsumption(BaseModel):
    counter_set: str | None = Field(
        default=None,
        serialization_alias="counterSet",
        validation_alias=AliasChoices("counter_set", "counterSet"),
    )

    counters: dict[str, V1beta1Counter] = Field(default={})

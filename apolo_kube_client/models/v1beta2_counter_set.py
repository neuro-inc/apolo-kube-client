from __future__ import annotations
from pydantic import BaseModel, Field
from .v1beta2_counter import V1beta2Counter

__all__ = ("V1beta2CounterSet",)


class V1beta2CounterSet(BaseModel):
    counters: dict[str, V1beta2Counter] = Field(
        default_factory=lambda: {}, alias="counters"
    )

    name: str | None = Field(default_factory=lambda: None, alias="name")

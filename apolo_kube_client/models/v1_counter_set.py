from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_counter import V1Counter

__all__ = ("V1CounterSet",)


class V1CounterSet(BaseModel):
    counters: dict[str, V1Counter] = Field(default_factory=lambda: {}, alias="counters")

    name: str | None = Field(default_factory=lambda: None, alias="name")

from __future__ import annotations
from pydantic import BaseModel, Field
from .v1beta1_counter import V1beta1Counter

__all__ = ("V1beta1CounterSet",)


class V1beta1CounterSet(BaseModel):
    counters: dict[str, V1beta1Counter] = Field(
        default_factory=lambda: {}, alias="counters"
    )

    name: str | None = Field(default_factory=lambda: None, alias="name")

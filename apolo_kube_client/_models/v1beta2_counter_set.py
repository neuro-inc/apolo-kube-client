from pydantic import BaseModel
from .v1beta2_counter import V1beta2Counter

__all__ = ("V1beta2CounterSet",)


class V1beta2CounterSet(BaseModel):
    counters: dict[str, V1beta2Counter] = {}

    name: str | None = None

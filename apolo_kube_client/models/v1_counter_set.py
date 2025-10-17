from pydantic import BaseModel
from .v1_counter import V1Counter

__all__ = ("V1CounterSet",)


class V1CounterSet(BaseModel):
    counters: dict[str, V1Counter] = {}

    name: str | None = None

from pydantic import BaseModel
from .v1beta1_counter import V1beta1Counter

__all__ = ("V1beta1CounterSet",)


class V1beta1CounterSet(BaseModel):
    counters: dict[str, V1beta1Counter] = {}

    name: str | None = None

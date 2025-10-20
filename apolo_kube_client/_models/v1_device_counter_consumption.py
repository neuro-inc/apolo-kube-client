from pydantic import AliasChoices, BaseModel, Field
from .v1_counter import V1Counter

__all__ = ("V1DeviceCounterConsumption",)


class V1DeviceCounterConsumption(BaseModel):
    counter_set: str | None = Field(
        default=None,
        serialization_alias="counterSet",
        validation_alias=AliasChoices("counter_set", "counterSet"),
    )

    counters: dict[str, V1Counter] = {}

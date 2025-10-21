from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .v1beta2_counter import V1beta2Counter
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1beta2DeviceCounterConsumption",)


class V1beta2DeviceCounterConsumption(BaseModel):
    counter_set: str | None = Field(
        default=None,
        serialization_alias="counterSet",
        validation_alias=AliasChoices("counter_set", "counterSet"),
    )

    counters: Annotated[
        dict[str, V1beta2Counter], BeforeValidator(_collection_if_none("{}"))
    ] = {}

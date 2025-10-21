from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .v1beta1_counter import V1beta1Counter
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1beta1DeviceCounterConsumption",)


class V1beta1DeviceCounterConsumption(BaseModel):
    counter_set: str | None = Field(
        default=None,
        serialization_alias="counterSet",
        validation_alias=AliasChoices("counter_set", "counterSet"),
    )

    counters: Annotated[
        dict[str, V1beta1Counter], BeforeValidator(_collection_if_none("{}"))
    ] = {}

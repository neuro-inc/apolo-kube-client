from pydantic import BaseModel
from .utils import _collection_if_none
from .v1beta2_counter import V1beta2Counter
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1beta2CounterSet",)


class V1beta2CounterSet(BaseModel):
    counters: Annotated[
        dict[str, V1beta2Counter], BeforeValidator(_collection_if_none("{}"))
    ] = {}

    name: str | None = None

from pydantic import BaseModel
from .utils import _collection_if_none
from .v1_counter import V1Counter
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1CounterSet",)


class V1CounterSet(BaseModel):
    counters: Annotated[
        dict[str, V1Counter], BeforeValidator(_collection_if_none("{}"))
    ] = {}

    name: str | None = None

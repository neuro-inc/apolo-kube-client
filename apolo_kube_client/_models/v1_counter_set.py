from pydantic import BaseModel, Field
from .utils import _collection_if_none
from .utils import _exclude_if
from .v1_counter import V1Counter
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1CounterSet",)


class V1CounterSet(BaseModel):
    counters: Annotated[
        dict[str, V1Counter], BeforeValidator(_collection_if_none("{}"))
    ] = Field(default={}, exclude_if=_exclude_if)

    name: str | None = Field(default=None, exclude_if=_exclude_if)

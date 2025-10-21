from pydantic import BaseModel
from .utils import _collection_if_none
from .v1beta1_counter import V1beta1Counter
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1beta1CounterSet",)


class V1beta1CounterSet(BaseModel):
    counters: Annotated[
        dict[str, V1beta1Counter], BeforeValidator(_collection_if_none("{}"))
    ] = {}

    name: str | None = None

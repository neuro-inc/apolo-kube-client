from pydantic import BaseModel
from .utils import _collection_if_none
from .v1_limit_range_item import V1LimitRangeItem
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1LimitRangeSpec",)


class V1LimitRangeSpec(BaseModel):
    limits: Annotated[
        list[V1LimitRangeItem], BeforeValidator(_collection_if_none("[]"))
    ] = []

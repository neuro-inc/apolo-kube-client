from pydantic import BaseModel, Field
from .utils import _collection_if_none
from .utils import _exclude_if
from .v1_limit_range_item import V1LimitRangeItem
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1LimitRangeSpec",)


class V1LimitRangeSpec(BaseModel):
    limits: Annotated[
        list[V1LimitRangeItem], BeforeValidator(_collection_if_none("[]"))
    ] = Field(default=[], exclude_if=_exclude_if)

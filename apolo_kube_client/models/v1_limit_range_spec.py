from pydantic import BaseModel
from .v1_limit_range_item import V1LimitRangeItem

__all__ = ("V1LimitRangeSpec",)


class V1LimitRangeSpec(BaseModel):
    limits: list[V1LimitRangeItem] = []

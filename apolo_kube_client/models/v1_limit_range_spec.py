from pydantic import BaseModel, Field

from .v1_limit_range_item import V1LimitRangeItem


class V1LimitRangeSpec(BaseModel):
    limits: list[V1LimitRangeItem] | None = Field(None, alias="limits")

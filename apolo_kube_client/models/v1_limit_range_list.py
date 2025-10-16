from __future__ import annotations

from pydantic import BaseModel, Field

from .v1_limit_range import V1LimitRange
from .v1_list_meta import V1ListMeta

__all__ = ("V1LimitRangeList",)


class V1LimitRangeList(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    items: list[V1LimitRange] | None = Field(None, alias="items")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ListMeta | None = Field(None, alias="metadata")

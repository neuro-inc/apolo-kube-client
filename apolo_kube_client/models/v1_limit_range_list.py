from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_limit_range import V1LimitRange
from .v1_list_meta import V1ListMeta

__all__ = ("V1LimitRangeList",)


class V1LimitRangeList(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    items: list[V1LimitRange] = Field(default=[])

    kind: str | None = Field(default=None)

    metadata: V1ListMeta

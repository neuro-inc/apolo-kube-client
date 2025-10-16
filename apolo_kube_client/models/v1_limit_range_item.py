from __future__ import annotations

from pydantic import BaseModel, Field

__all__ = ("V1LimitRangeItem",)


class V1LimitRangeItem(BaseModel):
    default: dict[str, str] | None = Field(None, alias="default")

    default_request: dict[str, str] | None = Field(None, alias="defaultRequest")

    max: dict[str, str] | None = Field(None, alias="max")

    max_limit_request_ratio: dict[str, str] | None = Field(
        None, alias="maxLimitRequestRatio"
    )

    min: dict[str, str] | None = Field(None, alias="min")

    type: str | None = Field(None, alias="type")

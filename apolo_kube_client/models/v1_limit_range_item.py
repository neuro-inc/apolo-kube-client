from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1LimitRangeItem",)


class V1LimitRangeItem(BaseModel):
    default: dict[str, str] = Field(default_factory=lambda: {})

    default_request: dict[str, str] = Field(
        default_factory=lambda: {}, alias="defaultRequest"
    )

    max: dict[str, str] = Field(default_factory=lambda: {})

    max_limit_request_ratio: dict[str, str] = Field(
        default_factory=lambda: {}, alias="maxLimitRequestRatio"
    )

    min: dict[str, str] = Field(default_factory=lambda: {})

    type: str | None = Field(default_factory=lambda: None)

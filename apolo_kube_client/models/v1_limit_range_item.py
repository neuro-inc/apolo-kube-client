from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field


__all__ = ("V1LimitRangeItem",)


class V1LimitRangeItem(BaseModel):
    default: dict[str, str] = Field(default={})

    default_request: dict[str, str] = Field(
        default={},
        serialization_alias="defaultRequest",
        validation_alias=AliasChoices("default_request", "defaultRequest"),
    )

    max: dict[str, str] = Field(default={})

    max_limit_request_ratio: dict[str, str] = Field(
        default={},
        serialization_alias="maxLimitRequestRatio",
        validation_alias=AliasChoices(
            "max_limit_request_ratio", "maxLimitRequestRatio"
        ),
    )

    min: dict[str, str] = Field(default={})

    type: str | None = Field(default=None)

from pydantic import AliasChoices, BaseModel, Field


__all__ = ("V1LimitRangeItem",)


class V1LimitRangeItem(BaseModel):
    default: dict[str, str] = {}

    default_request: dict[str, str] = Field(
        default={},
        serialization_alias="defaultRequest",
        validation_alias=AliasChoices("default_request", "defaultRequest"),
    )

    max: dict[str, str] = {}

    max_limit_request_ratio: dict[str, str] = Field(
        default={},
        serialization_alias="maxLimitRequestRatio",
        validation_alias=AliasChoices(
            "max_limit_request_ratio", "maxLimitRequestRatio"
        ),
    )

    min: dict[str, str] = {}

    type: str | None = None

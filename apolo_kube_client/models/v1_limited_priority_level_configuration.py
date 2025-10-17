from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_limit_response import V1LimitResponse

__all__ = ("V1LimitedPriorityLevelConfiguration",)


class V1LimitedPriorityLevelConfiguration(BaseModel):
    borrowing_limit_percent: int | None = Field(
        default=None,
        serialization_alias="borrowingLimitPercent",
        validation_alias=AliasChoices(
            "borrowing_limit_percent", "borrowingLimitPercent"
        ),
    )

    lendable_percent: int | None = Field(
        default=None,
        serialization_alias="lendablePercent",
        validation_alias=AliasChoices("lendable_percent", "lendablePercent"),
    )

    limit_response: V1LimitResponse = Field(
        default_factory=lambda: V1LimitResponse(),
        serialization_alias="limitResponse",
        validation_alias=AliasChoices("limit_response", "limitResponse"),
    )

    nominal_concurrency_shares: int | None = Field(
        default=None,
        serialization_alias="nominalConcurrencyShares",
        validation_alias=AliasChoices(
            "nominal_concurrency_shares", "nominalConcurrencyShares"
        ),
    )

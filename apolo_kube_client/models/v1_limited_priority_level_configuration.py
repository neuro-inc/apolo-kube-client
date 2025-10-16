from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_limit_response import V1LimitResponse

__all__ = ("V1LimitedPriorityLevelConfiguration",)


class V1LimitedPriorityLevelConfiguration(BaseModel):
    borrowing_limit_percent: int | None = Field(
        default_factory=lambda: None, alias="borrowingLimitPercent"
    )

    lendable_percent: int | None = Field(
        default_factory=lambda: None, alias="lendablePercent"
    )

    limit_response: V1LimitResponse = Field(
        default_factory=lambda: V1LimitResponse(), alias="limitResponse"
    )

    nominal_concurrency_shares: int | None = Field(
        default_factory=lambda: None, alias="nominalConcurrencyShares"
    )

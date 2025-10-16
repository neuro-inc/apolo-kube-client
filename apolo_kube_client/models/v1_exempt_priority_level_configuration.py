from __future__ import annotations

from pydantic import BaseModel, Field

__all__ = ("V1ExemptPriorityLevelConfiguration",)


class V1ExemptPriorityLevelConfiguration(BaseModel):
    lendable_percent: int | None = Field(None, alias="lendablePercent")

    nominal_concurrency_shares: int | None = Field(
        None, alias="nominalConcurrencyShares"
    )

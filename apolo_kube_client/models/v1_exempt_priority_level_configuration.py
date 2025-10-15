from pydantic import BaseModel, Field


class V1ExemptPriorityLevelConfiguration(BaseModel):
    lendable_percent: int | None = Field(None, alias="lendablePercent")

    nominal_concurrency_shares: int | None = Field(
        None, alias="nominalConcurrencyShares"
    )

from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field


__all__ = ("V1ExemptPriorityLevelConfiguration",)


class V1ExemptPriorityLevelConfiguration(BaseModel):
    lendable_percent: int | None = Field(
        default=None,
        serialization_alias="lendablePercent",
        validation_alias=AliasChoices("lendable_percent", "lendablePercent"),
    )

    nominal_concurrency_shares: int | None = Field(
        default=None,
        serialization_alias="nominalConcurrencyShares",
        validation_alias=AliasChoices(
            "nominal_concurrency_shares", "nominalConcurrencyShares"
        ),
    )

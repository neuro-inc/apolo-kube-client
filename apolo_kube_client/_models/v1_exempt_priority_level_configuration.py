from pydantic import AliasChoices, BaseModel, Field
from .utils import _exclude_if

__all__ = ("V1ExemptPriorityLevelConfiguration",)


class V1ExemptPriorityLevelConfiguration(BaseModel):
    lendable_percent: int | None = Field(
        default=None,
        serialization_alias="lendablePercent",
        validation_alias=AliasChoices("lendable_percent", "lendablePercent"),
        exclude_if=_exclude_if,
    )

    nominal_concurrency_shares: int | None = Field(
        default=None,
        serialization_alias="nominalConcurrencyShares",
        validation_alias=AliasChoices(
            "nominal_concurrency_shares", "nominalConcurrencyShares"
        ),
        exclude_if=_exclude_if,
    )

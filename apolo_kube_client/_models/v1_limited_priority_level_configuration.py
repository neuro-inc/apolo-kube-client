from pydantic import AliasChoices, BaseModel, Field
from .utils import _default_if_none
from .v1_limit_response import V1LimitResponse
from pydantic import BeforeValidator
from typing import Annotated

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

    limit_response: Annotated[
        V1LimitResponse, BeforeValidator(_default_if_none(V1LimitResponse))
    ] = Field(
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

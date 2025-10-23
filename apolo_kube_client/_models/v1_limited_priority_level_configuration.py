from pydantic import AliasChoices, BaseModel, Field
from .utils import _default_if_none
from .utils import _exclude_if
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
        exclude_if=_exclude_if,
    )

    lendable_percent: int | None = Field(
        default=None,
        serialization_alias="lendablePercent",
        validation_alias=AliasChoices("lendable_percent", "lendablePercent"),
        exclude_if=_exclude_if,
    )

    limit_response: Annotated[
        V1LimitResponse, BeforeValidator(_default_if_none(V1LimitResponse))
    ] = Field(
        default_factory=lambda: V1LimitResponse(),
        serialization_alias="limitResponse",
        validation_alias=AliasChoices("limit_response", "limitResponse"),
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

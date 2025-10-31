from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .v1_limit_response import V1LimitResponse

__all__ = ("V1LimitedPriorityLevelConfiguration",)


class V1LimitedPriorityLevelConfiguration(BaseModel):
    """LimitedPriorityLevelConfiguration specifies how to handle requests that are subject to limits. It addresses two issues:
    - How are requests for this priority level limited?
    - What should be done with requests that exceed the limit?"""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.flowcontrol.v1.LimitedPriorityLevelConfiguration"
    )

    borrowing_limit_percent: Annotated[
        int | None,
        Field(
            alias="borrowingLimitPercent",
            description="""`borrowingLimitPercent`, if present, configures a limit on how many seats this priority level can borrow from other priority levels. The limit is known as this level's BorrowingConcurrencyLimit (BorrowingCL) and is a limit on the total number of seats that this level may borrow at any one time. This field holds the ratio of that limit to the level's nominal concurrency limit. When this field is non-nil, it must hold a non-negative integer and the limit is calculated as follows.

BorrowingCL(i) = round( NominalCL(i) * borrowingLimitPercent(i)/100.0 )

The value of this field can be more than 100, implying that this priority level can borrow a number of seats that is greater than its own nominal concurrency limit (NominalCL). When this field is left `nil`, the limit is effectively infinite.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    lendable_percent: Annotated[
        int | None,
        Field(
            alias="lendablePercent",
            description="""`lendablePercent` prescribes the fraction of the level's NominalCL that can be borrowed by other priority levels. The value of this field must be between 0 and 100, inclusive, and it defaults to 0. The number of seats that other levels can borrow from this level, known as this level's LendableConcurrencyLimit (LendableCL), is defined as follows.

LendableCL(i) = round( NominalCL(i) * lendablePercent(i)/100.0 )""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    limit_response: Annotated[
        V1LimitResponse | None,
        Field(
            alias="limitResponse",
            description="""`limitResponse` indicates what to do with requests that can not be executed right now""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    nominal_concurrency_shares: Annotated[
        int | None,
        Field(
            alias="nominalConcurrencyShares",
            description="""`nominalConcurrencyShares` (NCS) contributes to the computation of the NominalConcurrencyLimit (NominalCL) of this level. This is the number of execution seats available at this priority level. This is used both for requests dispatched from this priority level as well as requests dispatched from other priority levels borrowing seats from this level. The server's concurrency limit (ServerCL) is divided among the Limited priority levels in proportion to their NCS values:

NominalCL(i)  = ceil( ServerCL * NCS(i) / sum_ncs ) sum_ncs = sum[priority level k] NCS(k)

Bigger numbers mean a larger nominal concurrency limit, at the expense of every other priority level.

If not specified, this field defaults to a value of 30.

Setting this field to zero supports the construction of a "jail" for this priority level that is used to hold some request(s)""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

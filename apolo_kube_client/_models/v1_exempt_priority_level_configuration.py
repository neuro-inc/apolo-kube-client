from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("V1ExemptPriorityLevelConfiguration",)


class V1ExemptPriorityLevelConfiguration(BaseModel):
    """ExemptPriorityLevelConfiguration describes the configurable aspects of the handling of exempt requests. In the mandatory exempt configuration object the values in the fields here can be modified by authorized users, unlike the rest of the `spec`."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.flowcontrol.v1.ExemptPriorityLevelConfiguration"
    )

    lendable_percent: Annotated[
        int | None,
        Field(
            alias="lendablePercent",
            description="""`lendablePercent` prescribes the fraction of the level's NominalCL that can be borrowed by other priority levels.  This value of this field must be between 0 and 100, inclusive, and it defaults to 0. The number of seats that other levels can borrow from this level, known as this level's LendableConcurrencyLimit (LendableCL), is defined as follows.

LendableCL(i) = round( NominalCL(i) * lendablePercent(i)/100.0 )""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    nominal_concurrency_shares: Annotated[
        int | None,
        Field(
            alias="nominalConcurrencyShares",
            description="""`nominalConcurrencyShares` (NCS) contributes to the computation of the NominalConcurrencyLimit (NominalCL) of this level. This is the number of execution seats nominally reserved for this priority level. This DOES NOT limit the dispatching from this priority level but affects the other priority levels through the borrowing mechanism. The server's concurrency limit (ServerCL) is divided among all the priority levels in proportion to their NCS values:

NominalCL(i)  = ceil( ServerCL * NCS(i) / sum_ncs ) sum_ncs = sum[priority level k] NCS(k)

Bigger numbers mean a larger nominal concurrency limit, at the expense of every other priority level. This field has a default value of zero.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

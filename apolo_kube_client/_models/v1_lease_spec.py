from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime

__all__ = ("V1LeaseSpec",)


class V1LeaseSpec(BaseModel):
    """LeaseSpec is a specification of a Lease."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.coordination.v1.LeaseSpec"

    acquire_time: Annotated[
        datetime | None,
        Field(
            alias="acquireTime",
            description="""acquireTime is a time when the current lease was acquired.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    holder_identity: Annotated[
        str | None,
        Field(
            alias="holderIdentity",
            description="""holderIdentity contains the identity of the holder of a current lease. If Coordinated Leader Election is used, the holder identity must be equal to the elected LeaseCandidate.metadata.name field.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    lease_duration_seconds: Annotated[
        int | None,
        Field(
            alias="leaseDurationSeconds",
            description="""leaseDurationSeconds is a duration that candidates for a lease need to wait to force acquire it. This is measured against the time of last observed renewTime.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    lease_transitions: Annotated[
        int | None,
        Field(
            alias="leaseTransitions",
            description="""leaseTransitions is the number of transitions of a lease between holders.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    preferred_holder: Annotated[
        str | None,
        Field(
            alias="preferredHolder",
            description="""PreferredHolder signals to a lease holder that the lease has a more optimal holder and should be given up. This field can only be set if Strategy is also set.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    renew_time: Annotated[
        datetime | None,
        Field(
            alias="renewTime",
            description="""renewTime is a time when the current holder of a lease has last updated the lease.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    strategy: Annotated[
        str | None,
        Field(
            description="""Strategy indicates the strategy for picking the leader for coordinated leader election. If the field is not specified, there is no active coordination for this lease. (Alpha) Using this field requires the CoordinatedLeaderElection feature gate to be enabled.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

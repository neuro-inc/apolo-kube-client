from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime

__all__ = ("V1alpha2LeaseCandidateSpec",)


class V1alpha2LeaseCandidateSpec(BaseModel):
    """LeaseCandidateSpec is a specification of a Lease."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.coordination.v1alpha2.LeaseCandidateSpec"
    )

    binary_version: Annotated[
        str,
        Field(
            alias="binaryVersion",
            description="""BinaryVersion is the binary version. It must be in a semver format without leading `v`. This field is required.""",
        ),
    ]

    emulation_version: Annotated[
        str | None,
        Field(
            alias="emulationVersion",
            description='''EmulationVersion is the emulation version. It must be in a semver format without leading `v`. EmulationVersion must be less than or equal to BinaryVersion. This field is required when strategy is "OldestEmulationVersion"''',
            exclude_if=lambda v: v is None,
        ),
    ] = None

    lease_name: Annotated[
        str,
        Field(
            alias="leaseName",
            description="""LeaseName is the name of the lease for which this candidate is contending. This field is immutable.""",
        ),
    ]

    ping_time: Annotated[
        datetime | None,
        Field(
            alias="pingTime",
            description="""PingTime is the last time that the server has requested the LeaseCandidate to renew. It is only done during leader election to check if any LeaseCandidates have become ineligible. When PingTime is updated, the LeaseCandidate will respond by updating RenewTime.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    renew_time: Annotated[
        datetime | None,
        Field(
            alias="renewTime",
            description="""RenewTime is the time that the LeaseCandidate was last updated. Any time a Lease needs to do leader election, the PingTime field is updated to signal to the LeaseCandidate that they should update the RenewTime. Old LeaseCandidate objects are also garbage collected if it has been hours since the last renew. The PingTime field is updated regularly to prevent garbage collection for still active LeaseCandidates.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    strategy: Annotated[
        str,
        Field(
            description="""Strategy is the strategy that coordinated leader election will use for picking the leader. If multiple candidates for the same Lease return different strategies, the strategy provided by the candidate with the latest BinaryVersion will be used. If there is still conflict, this is a user error and coordinated leader election will not operate the Lease until resolved."""
        ),
    ]

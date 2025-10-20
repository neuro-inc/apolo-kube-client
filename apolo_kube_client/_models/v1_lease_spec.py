from pydantic import AliasChoices, BaseModel, Field
from datetime import datetime

__all__ = ("V1LeaseSpec",)


class V1LeaseSpec(BaseModel):
    acquire_time: datetime | None = Field(
        default=None,
        serialization_alias="acquireTime",
        validation_alias=AliasChoices("acquire_time", "acquireTime"),
    )

    holder_identity: str | None = Field(
        default=None,
        serialization_alias="holderIdentity",
        validation_alias=AliasChoices("holder_identity", "holderIdentity"),
    )

    lease_duration_seconds: int | None = Field(
        default=None,
        serialization_alias="leaseDurationSeconds",
        validation_alias=AliasChoices("lease_duration_seconds", "leaseDurationSeconds"),
    )

    lease_transitions: int | None = Field(
        default=None,
        serialization_alias="leaseTransitions",
        validation_alias=AliasChoices("lease_transitions", "leaseTransitions"),
    )

    preferred_holder: str | None = Field(
        default=None,
        serialization_alias="preferredHolder",
        validation_alias=AliasChoices("preferred_holder", "preferredHolder"),
    )

    renew_time: datetime | None = Field(
        default=None,
        serialization_alias="renewTime",
        validation_alias=AliasChoices("renew_time", "renewTime"),
    )

    strategy: str | None = None

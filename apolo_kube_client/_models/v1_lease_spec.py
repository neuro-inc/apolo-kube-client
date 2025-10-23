from pydantic import AliasChoices, BaseModel, Field
from .utils import _exclude_if
from datetime import datetime

__all__ = ("V1LeaseSpec",)


class V1LeaseSpec(BaseModel):
    acquire_time: datetime | None = Field(
        default=None,
        serialization_alias="acquireTime",
        validation_alias=AliasChoices("acquire_time", "acquireTime"),
        exclude_if=_exclude_if,
    )

    holder_identity: str | None = Field(
        default=None,
        serialization_alias="holderIdentity",
        validation_alias=AliasChoices("holder_identity", "holderIdentity"),
        exclude_if=_exclude_if,
    )

    lease_duration_seconds: int | None = Field(
        default=None,
        serialization_alias="leaseDurationSeconds",
        validation_alias=AliasChoices("lease_duration_seconds", "leaseDurationSeconds"),
        exclude_if=_exclude_if,
    )

    lease_transitions: int | None = Field(
        default=None,
        serialization_alias="leaseTransitions",
        validation_alias=AliasChoices("lease_transitions", "leaseTransitions"),
        exclude_if=_exclude_if,
    )

    preferred_holder: str | None = Field(
        default=None,
        serialization_alias="preferredHolder",
        validation_alias=AliasChoices("preferred_holder", "preferredHolder"),
        exclude_if=_exclude_if,
    )

    renew_time: datetime | None = Field(
        default=None,
        serialization_alias="renewTime",
        validation_alias=AliasChoices("renew_time", "renewTime"),
        exclude_if=_exclude_if,
    )

    strategy: str | None = Field(default=None, exclude_if=_exclude_if)

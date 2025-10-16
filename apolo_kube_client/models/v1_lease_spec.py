from __future__ import annotations
from pydantic import BaseModel, Field
from datetime import datetime

__all__ = ("V1LeaseSpec",)


class V1LeaseSpec(BaseModel):
    acquire_time: datetime | None = Field(
        default_factory=lambda: None, alias="acquireTime"
    )

    holder_identity: str | None = Field(
        default_factory=lambda: None, alias="holderIdentity"
    )

    lease_duration_seconds: int | None = Field(
        default_factory=lambda: None, alias="leaseDurationSeconds"
    )

    lease_transitions: int | None = Field(
        default_factory=lambda: None, alias="leaseTransitions"
    )

    preferred_holder: str | None = Field(
        default_factory=lambda: None, alias="preferredHolder"
    )

    renew_time: datetime | None = Field(default_factory=lambda: None, alias="renewTime")

    strategy: str | None = Field(default_factory=lambda: None, alias="strategy")

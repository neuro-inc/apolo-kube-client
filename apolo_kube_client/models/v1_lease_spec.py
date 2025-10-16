from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field

__all__ = ("V1LeaseSpec",)


class V1LeaseSpec(BaseModel):
    acquire_time: datetime | None = Field(None, alias="acquireTime")

    holder_identity: str | None = Field(None, alias="holderIdentity")

    lease_duration_seconds: int | None = Field(None, alias="leaseDurationSeconds")

    lease_transitions: int | None = Field(None, alias="leaseTransitions")

    preferred_holder: str | None = Field(None, alias="preferredHolder")

    renew_time: datetime | None = Field(None, alias="renewTime")

    strategy: str | None = Field(None, alias="strategy")

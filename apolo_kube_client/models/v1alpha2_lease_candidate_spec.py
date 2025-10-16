from __future__ import annotations
from pydantic import BaseModel, Field
from datetime import datetime

__all__ = ("V1alpha2LeaseCandidateSpec",)


class V1alpha2LeaseCandidateSpec(BaseModel):
    binary_version: str | None = Field(
        default_factory=lambda: None, alias="binaryVersion"
    )

    emulation_version: str | None = Field(
        default_factory=lambda: None, alias="emulationVersion"
    )

    lease_name: str | None = Field(default_factory=lambda: None, alias="leaseName")

    ping_time: datetime | None = Field(default_factory=lambda: None, alias="pingTime")

    renew_time: datetime | None = Field(default_factory=lambda: None, alias="renewTime")

    strategy: str | None = Field(default_factory=lambda: None, alias="strategy")

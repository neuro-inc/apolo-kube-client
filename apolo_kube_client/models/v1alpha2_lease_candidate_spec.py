from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from datetime import datetime

__all__ = ("V1alpha2LeaseCandidateSpec",)


class V1alpha2LeaseCandidateSpec(BaseModel):
    binary_version: str | None = Field(
        default=None,
        serialization_alias="binaryVersion",
        validation_alias=AliasChoices("binary_version", "binaryVersion"),
    )

    emulation_version: str | None = Field(
        default=None,
        serialization_alias="emulationVersion",
        validation_alias=AliasChoices("emulation_version", "emulationVersion"),
    )

    lease_name: str | None = Field(
        default=None,
        serialization_alias="leaseName",
        validation_alias=AliasChoices("lease_name", "leaseName"),
    )

    ping_time: datetime | None = Field(
        default=None,
        serialization_alias="pingTime",
        validation_alias=AliasChoices("ping_time", "pingTime"),
    )

    renew_time: datetime | None = Field(
        default=None,
        serialization_alias="renewTime",
        validation_alias=AliasChoices("renew_time", "renewTime"),
    )

    strategy: str | None = Field(default=None)

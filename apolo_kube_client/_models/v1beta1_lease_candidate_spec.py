from pydantic import AliasChoices, BaseModel, Field
from .utils import _exclude_if
from datetime import datetime

__all__ = ("V1beta1LeaseCandidateSpec",)


class V1beta1LeaseCandidateSpec(BaseModel):
    binary_version: str | None = Field(
        default=None,
        serialization_alias="binaryVersion",
        validation_alias=AliasChoices("binary_version", "binaryVersion"),
        exclude_if=_exclude_if,
    )

    emulation_version: str | None = Field(
        default=None,
        serialization_alias="emulationVersion",
        validation_alias=AliasChoices("emulation_version", "emulationVersion"),
        exclude_if=_exclude_if,
    )

    lease_name: str | None = Field(
        default=None,
        serialization_alias="leaseName",
        validation_alias=AliasChoices("lease_name", "leaseName"),
        exclude_if=_exclude_if,
    )

    ping_time: datetime | None = Field(
        default=None,
        serialization_alias="pingTime",
        validation_alias=AliasChoices("ping_time", "pingTime"),
        exclude_if=_exclude_if,
    )

    renew_time: datetime | None = Field(
        default=None,
        serialization_alias="renewTime",
        validation_alias=AliasChoices("renew_time", "renewTime"),
        exclude_if=_exclude_if,
    )

    strategy: str | None = Field(default=None, exclude_if=_exclude_if)

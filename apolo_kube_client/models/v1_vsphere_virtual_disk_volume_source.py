from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field


__all__ = ("V1VsphereVirtualDiskVolumeSource",)


class V1VsphereVirtualDiskVolumeSource(BaseModel):
    fs_type: str | None = Field(
        default=None,
        serialization_alias="fsType",
        validation_alias=AliasChoices("fs_type", "fsType"),
    )

    storage_policy_id: str | None = Field(
        default=None,
        serialization_alias="storagePolicyID",
        validation_alias=AliasChoices("storage_policy_id", "storagePolicyID"),
    )

    storage_policy_name: str | None = Field(
        default=None,
        serialization_alias="storagePolicyName",
        validation_alias=AliasChoices("storage_policy_name", "storagePolicyName"),
    )

    volume_path: str | None = Field(
        default=None,
        serialization_alias="volumePath",
        validation_alias=AliasChoices("volume_path", "volumePath"),
    )

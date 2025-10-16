from __future__ import annotations

from pydantic import BaseModel, Field

__all__ = ("V1VsphereVirtualDiskVolumeSource",)


class V1VsphereVirtualDiskVolumeSource(BaseModel):
    fs_type: str | None = Field(None, alias="fsType")

    storage_policy_id: str | None = Field(None, alias="storagePolicyID")

    storage_policy_name: str | None = Field(None, alias="storagePolicyName")

    volume_path: str | None = Field(None, alias="volumePath")

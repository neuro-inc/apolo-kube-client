from __future__ import annotations

from pydantic import BaseModel, Field

__all__ = ("V1PhotonPersistentDiskVolumeSource",)


class V1PhotonPersistentDiskVolumeSource(BaseModel):
    fs_type: str | None = Field(None, alias="fsType")

    pd_id: str | None = Field(None, alias="pdID")

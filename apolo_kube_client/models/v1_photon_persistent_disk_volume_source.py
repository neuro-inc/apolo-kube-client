from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field


__all__ = ("V1PhotonPersistentDiskVolumeSource",)


class V1PhotonPersistentDiskVolumeSource(BaseModel):
    fs_type: str | None = Field(
        default=None,
        serialization_alias="fsType",
        validation_alias=AliasChoices("fs_type", "fsType"),
    )

    pd_id: str | None = Field(
        default=None,
        serialization_alias="pdID",
        validation_alias=AliasChoices("pd_id", "pdID"),
    )

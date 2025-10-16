from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_local_object_reference import V1LocalObjectReference

__all__ = ("V1CinderVolumeSource",)


class V1CinderVolumeSource(BaseModel):
    fs_type: str | None = Field(default_factory=lambda: None, alias="fsType")

    read_only: bool | None = Field(default_factory=lambda: None, alias="readOnly")

    secret_ref: V1LocalObjectReference = Field(
        default_factory=lambda: V1LocalObjectReference(), alias="secretRef"
    )

    volume_id: str | None = Field(default_factory=lambda: None, alias="volumeID")

from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_local_object_reference import V1LocalObjectReference

__all__ = ("V1StorageOSVolumeSource",)


class V1StorageOSVolumeSource(BaseModel):
    fs_type: str | None = Field(default_factory=lambda: None, alias="fsType")

    read_only: bool | None = Field(default_factory=lambda: None, alias="readOnly")

    secret_ref: V1LocalObjectReference = Field(
        default_factory=lambda: V1LocalObjectReference(), alias="secretRef"
    )

    volume_name: str | None = Field(default_factory=lambda: None, alias="volumeName")

    volume_namespace: str | None = Field(
        default_factory=lambda: None, alias="volumeNamespace"
    )

from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_object_reference import V1ObjectReference

__all__ = ("V1StorageOSPersistentVolumeSource",)


class V1StorageOSPersistentVolumeSource(BaseModel):
    fs_type: str | None = Field(default_factory=lambda: None, alias="fsType")

    read_only: bool | None = Field(default_factory=lambda: None, alias="readOnly")

    secret_ref: V1ObjectReference = Field(
        default_factory=lambda: V1ObjectReference(), alias="secretRef"
    )

    volume_name: str | None = Field(default_factory=lambda: None, alias="volumeName")

    volume_namespace: str | None = Field(
        default_factory=lambda: None, alias="volumeNamespace"
    )

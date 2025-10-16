from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_persistent_volume_spec import V1PersistentVolumeSpec

__all__ = ("V1VolumeAttachmentSource",)


class V1VolumeAttachmentSource(BaseModel):
    inline_volume_spec: V1PersistentVolumeSpec = Field(
        default_factory=lambda: V1PersistentVolumeSpec(), alias="inlineVolumeSpec"
    )

    persistent_volume_name: str | None = Field(
        default_factory=lambda: None, alias="persistentVolumeName"
    )

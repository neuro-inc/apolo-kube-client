from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_local_object_reference import V1LocalObjectReference

__all__ = ("V1CSIVolumeSource",)


class V1CSIVolumeSource(BaseModel):
    driver: str | None = Field(default_factory=lambda: None, alias="driver")

    fs_type: str | None = Field(default_factory=lambda: None, alias="fsType")

    node_publish_secret_ref: V1LocalObjectReference = Field(
        default_factory=lambda: V1LocalObjectReference(), alias="nodePublishSecretRef"
    )

    read_only: bool | None = Field(default_factory=lambda: None, alias="readOnly")

    volume_attributes: dict[str, str] = Field(
        default_factory=lambda: {}, alias="volumeAttributes"
    )

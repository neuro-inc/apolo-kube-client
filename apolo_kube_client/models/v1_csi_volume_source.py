from __future__ import annotations

from pydantic import BaseModel, Field

from .v1_local_object_reference import V1LocalObjectReference

__all__ = ("V1CSIVolumeSource",)


class V1CSIVolumeSource(BaseModel):
    driver: str | None = Field(None, alias="driver")

    fs_type: str | None = Field(None, alias="fsType")

    node_publish_secret_ref: V1LocalObjectReference | None = Field(
        None, alias="nodePublishSecretRef"
    )

    read_only: bool | None = Field(None, alias="readOnly")

    volume_attributes: dict[str, str] | None = Field(None, alias="volumeAttributes")

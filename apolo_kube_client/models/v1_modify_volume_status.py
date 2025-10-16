from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1ModifyVolumeStatus",)


class V1ModifyVolumeStatus(BaseModel):
    status: str | None = Field(default_factory=lambda: None, alias="status")

    target_volume_attributes_class_name: str | None = Field(
        default_factory=lambda: None, alias="targetVolumeAttributesClassName"
    )

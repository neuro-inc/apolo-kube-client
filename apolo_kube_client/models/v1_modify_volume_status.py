from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field


__all__ = ("V1ModifyVolumeStatus",)


class V1ModifyVolumeStatus(BaseModel):
    status: str | None = Field(default=None)

    target_volume_attributes_class_name: str | None = Field(
        default=None,
        serialization_alias="targetVolumeAttributesClassName",
        validation_alias=AliasChoices(
            "target_volume_attributes_class_name", "targetVolumeAttributesClassName"
        ),
    )

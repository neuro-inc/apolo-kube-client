from pydantic import AliasChoices, BaseModel, Field
from .utils import _exclude_if

__all__ = ("V1ModifyVolumeStatus",)


class V1ModifyVolumeStatus(BaseModel):
    status: str | None = Field(default=None, exclude_if=_exclude_if)

    target_volume_attributes_class_name: str | None = Field(
        default=None,
        serialization_alias="targetVolumeAttributesClassName",
        validation_alias=AliasChoices(
            "target_volume_attributes_class_name", "targetVolumeAttributesClassName"
        ),
        exclude_if=_exclude_if,
    )

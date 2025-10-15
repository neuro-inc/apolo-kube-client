from pydantic import BaseModel, Field


class V1ModifyVolumeStatus(BaseModel):
    status: str | None = Field(None, alias="status")

    target_volume_attributes_class_name: str | None = Field(
        None, alias="targetVolumeAttributesClassName"
    )

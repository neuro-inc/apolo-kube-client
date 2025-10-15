from pydantic import BaseModel, Field

from .v1_local_object_reference import V1LocalObjectReference


class V1CinderVolumeSource(BaseModel):
    fs_type: str | None = Field(None, alias="fsType")

    read_only: bool | None = Field(None, alias="readOnly")

    secret_ref: V1LocalObjectReference | None = Field(None, alias="secretRef")

    volume_id: str | None = Field(None, alias="volumeID")

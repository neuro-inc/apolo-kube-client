from pydantic import BaseModel, Field


class V1PortworxVolumeSource(BaseModel):
    fs_type: str | None = Field(None, alias="fsType")

    read_only: bool | None = Field(None, alias="readOnly")

    volume_id: str | None = Field(None, alias="volumeID")

from pydantic import BaseModel, Field


class V1LocalVolumeSource(BaseModel):
    fs_type: str | None = Field(None, alias="fsType")

    path: str | None = Field(None, alias="path")

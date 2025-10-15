from pydantic import BaseModel, Field


class V1VolumeDevice(BaseModel):
    device_path: str | None = Field(None, alias="devicePath")

    name: str | None = Field(None, alias="name")

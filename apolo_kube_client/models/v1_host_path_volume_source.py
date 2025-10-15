from pydantic import BaseModel, Field


class V1HostPathVolumeSource(BaseModel):
    path: str | None = Field(None, alias="path")

    type: str | None = Field(None, alias="type")

from pydantic import BaseModel, Field


class V1EmptyDirVolumeSource(BaseModel):
    medium: str | None = Field(None, alias="medium")

    size_limit: str | None = Field(None, alias="sizeLimit")

from pydantic import BaseModel, Field


class V1GlusterfsVolumeSource(BaseModel):
    endpoints: str | None = Field(None, alias="endpoints")

    path: str | None = Field(None, alias="path")

    read_only: bool | None = Field(None, alias="readOnly")

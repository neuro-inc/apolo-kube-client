from pydantic import BaseModel, Field


class V1VolumeNodeResources(BaseModel):
    count: int | None = Field(None, alias="count")

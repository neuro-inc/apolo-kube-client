from pydantic import BaseModel, Field


class V1VolumeResourceRequirements(BaseModel):
    limits: dict(str, str) | None = Field(None, alias="limits")

    requests: dict(str, str) | None = Field(None, alias="requests")

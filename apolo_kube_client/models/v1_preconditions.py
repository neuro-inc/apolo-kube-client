from pydantic import BaseModel, Field


class V1Preconditions(BaseModel):
    resource_version: str | None = Field(None, alias="resourceVersion")

    uid: str | None = Field(None, alias="uid")

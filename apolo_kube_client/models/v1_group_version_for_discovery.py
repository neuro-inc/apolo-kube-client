from pydantic import BaseModel, Field


class V1GroupVersionForDiscovery(BaseModel):
    group_version: str | None = Field(None, alias="groupVersion")

    version: str | None = Field(None, alias="version")

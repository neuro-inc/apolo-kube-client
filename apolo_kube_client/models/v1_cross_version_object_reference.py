from pydantic import BaseModel, Field


class V1CrossVersionObjectReference(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    kind: str | None = Field(None, alias="kind")

    name: str | None = Field(None, alias="name")

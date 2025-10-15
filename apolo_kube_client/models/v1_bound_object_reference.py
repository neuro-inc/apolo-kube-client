from pydantic import BaseModel, Field


class V1BoundObjectReference(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    kind: str | None = Field(None, alias="kind")

    name: str | None = Field(None, alias="name")

    uid: str | None = Field(None, alias="uid")

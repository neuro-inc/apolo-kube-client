from pydantic import BaseModel, Field


class V1ObjectFieldSelector(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    field_path: str | None = Field(None, alias="fieldPath")

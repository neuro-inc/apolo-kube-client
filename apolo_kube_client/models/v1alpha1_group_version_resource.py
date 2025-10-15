from pydantic import BaseModel, Field


class V1alpha1GroupVersionResource(BaseModel):
    group: str | None = Field(None, alias="group")

    resource: str | None = Field(None, alias="resource")

    version: str | None = Field(None, alias="version")

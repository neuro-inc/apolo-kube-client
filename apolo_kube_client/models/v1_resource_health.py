from pydantic import BaseModel, Field


class V1ResourceHealth(BaseModel):
    health: str | None = Field(None, alias="health")

    resource_id: str | None = Field(None, alias="resourceID")

from pydantic import BaseModel, Field


class V1PriorityLevelConfigurationReference(BaseModel):
    name: str | None = Field(None, alias="name")

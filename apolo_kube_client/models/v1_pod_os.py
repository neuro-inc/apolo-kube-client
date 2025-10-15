from pydantic import BaseModel, Field


class V1PodOS(BaseModel):
    name: str | None = Field(None, alias="name")

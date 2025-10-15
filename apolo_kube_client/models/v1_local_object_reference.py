from pydantic import BaseModel, Field


class V1LocalObjectReference(BaseModel):
    name: str | None = Field(None, alias="name")

from pydantic import BaseModel, Field


class V1ForZone(BaseModel):
    name: str | None = Field(None, alias="name")

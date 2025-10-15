from pydantic import BaseModel, Field


class V1PodSchedulingGate(BaseModel):
    name: str | None = Field(None, alias="name")

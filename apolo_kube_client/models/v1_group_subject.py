from pydantic import BaseModel, Field


class V1GroupSubject(BaseModel):
    name: str | None = Field(None, alias="name")

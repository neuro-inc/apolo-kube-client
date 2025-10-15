from pydantic import BaseModel, Field


class V1UserSubject(BaseModel):
    name: str | None = Field(None, alias="name")

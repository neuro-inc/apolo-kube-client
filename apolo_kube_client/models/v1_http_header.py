from pydantic import BaseModel, Field


class V1HTTPHeader(BaseModel):
    name: str | None = Field(None, alias="name")

    value: str | None = Field(None, alias="value")

from pydantic import BaseModel, Field


class V1Sysctl(BaseModel):
    name: str | None = Field(None, alias="name")

    value: str | None = Field(None, alias="value")

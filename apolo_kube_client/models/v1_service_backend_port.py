from pydantic import BaseModel, Field


class V1ServiceBackendPort(BaseModel):
    name: str | None = Field(None, alias="name")

    number: int | None = Field(None, alias="number")

from pydantic import BaseModel, Field


class V1EndpointConditions(BaseModel):
    ready: bool | None = Field(None, alias="ready")

    serving: bool | None = Field(None, alias="serving")

    terminating: bool | None = Field(None, alias="terminating")

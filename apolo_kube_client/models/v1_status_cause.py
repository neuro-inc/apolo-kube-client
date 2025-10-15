from pydantic import BaseModel, Field


class V1StatusCause(BaseModel):
    field: str | None = Field(None, alias="field")

    message: str | None = Field(None, alias="message")

    reason: str | None = Field(None, alias="reason")

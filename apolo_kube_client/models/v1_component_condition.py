from pydantic import BaseModel, Field


class V1ComponentCondition(BaseModel):
    error: str | None = Field(None, alias="error")

    message: str | None = Field(None, alias="message")

    status: str | None = Field(None, alias="status")

    type: str | None = Field(None, alias="type")

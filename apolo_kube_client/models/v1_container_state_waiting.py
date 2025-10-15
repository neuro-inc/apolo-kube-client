from pydantic import BaseModel, Field


class V1ContainerStateWaiting(BaseModel):
    message: str | None = Field(None, alias="message")

    reason: str | None = Field(None, alias="reason")

from datetime import datetime

from pydantic import BaseModel, Field


class V1VolumeError(BaseModel):
    message: str | None = Field(None, alias="message")

    time: datetime | None = Field(None, alias="time")

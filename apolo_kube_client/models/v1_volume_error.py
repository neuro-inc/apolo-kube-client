from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field

__all__ = ("V1VolumeError",)


class V1VolumeError(BaseModel):
    message: str | None = Field(None, alias="message")

    time: datetime | None = Field(None, alias="time")

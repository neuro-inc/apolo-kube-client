from __future__ import annotations
from pydantic import BaseModel, Field
from datetime import datetime

__all__ = ("V1VolumeError",)


class V1VolumeError(BaseModel):
    error_code: int | None = Field(default_factory=lambda: None, alias="errorCode")

    message: str | None = Field(default_factory=lambda: None)

    time: datetime | None = Field(default_factory=lambda: None)

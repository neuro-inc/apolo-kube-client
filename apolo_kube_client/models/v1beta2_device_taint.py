from __future__ import annotations
from pydantic import BaseModel, Field
from datetime import datetime

__all__ = ("V1beta2DeviceTaint",)


class V1beta2DeviceTaint(BaseModel):
    effect: str | None = Field(default_factory=lambda: None)

    key: str | None = Field(default_factory=lambda: None)

    time_added: datetime | None = Field(default_factory=lambda: None, alias="timeAdded")

    value: str | None = Field(default_factory=lambda: None)

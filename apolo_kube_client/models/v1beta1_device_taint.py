from __future__ import annotations
from pydantic import BaseModel, Field
from datetime import datetime

__all__ = ("V1beta1DeviceTaint",)


class V1beta1DeviceTaint(BaseModel):
    effect: str | None = Field(default_factory=lambda: None, alias="effect")

    key: str | None = Field(default_factory=lambda: None, alias="key")

    time_added: datetime | None = Field(default_factory=lambda: None, alias="timeAdded")

    value: str | None = Field(default_factory=lambda: None, alias="value")

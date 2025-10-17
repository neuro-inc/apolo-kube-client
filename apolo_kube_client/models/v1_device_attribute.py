from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1DeviceAttribute",)


class V1DeviceAttribute(BaseModel):
    bool: bool | None = Field(default_factory=lambda: None)

    int: int | None = Field(default_factory=lambda: None)

    string: str | None = Field(default_factory=lambda: None)

    version: str | None = Field(default_factory=lambda: None)

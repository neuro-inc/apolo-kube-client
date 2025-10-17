from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1beta2DeviceAttribute",)


class V1beta2DeviceAttribute(BaseModel):
    bool: bool | None = Field(default=None)

    int: int | None = Field(default=None)

    string: str | None = Field(default=None)

    version: str | None = Field(default=None)

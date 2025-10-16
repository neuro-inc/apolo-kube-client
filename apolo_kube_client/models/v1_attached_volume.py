from __future__ import annotations

from pydantic import BaseModel, Field

__all__ = ("V1AttachedVolume",)


class V1AttachedVolume(BaseModel):
    device_path: str | None = Field(None, alias="devicePath")

    name: str | None = Field(None, alias="name")

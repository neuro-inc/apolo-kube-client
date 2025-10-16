from __future__ import annotations

from pydantic import BaseModel, Field

__all__ = ("V1LocalVolumeSource",)


class V1LocalVolumeSource(BaseModel):
    fs_type: str | None = Field(None, alias="fsType")

    path: str | None = Field(None, alias="path")

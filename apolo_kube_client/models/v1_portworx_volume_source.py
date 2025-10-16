from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1PortworxVolumeSource",)


class V1PortworxVolumeSource(BaseModel):
    fs_type: str | None = Field(default_factory=lambda: None, alias="fsType")

    read_only: bool | None = Field(default_factory=lambda: None, alias="readOnly")

    volume_id: str | None = Field(default_factory=lambda: None, alias="volumeID")

from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1FCVolumeSource",)


class V1FCVolumeSource(BaseModel):
    fs_type: str | None = Field(default_factory=lambda: None, alias="fsType")

    lun: int | None = Field(default_factory=lambda: None)

    read_only: bool | None = Field(default_factory=lambda: None, alias="readOnly")

    target_ww_ns: list[str] = Field(default_factory=lambda: [], alias="targetWWNs")

    wwids: list[str] = Field(default_factory=lambda: [])

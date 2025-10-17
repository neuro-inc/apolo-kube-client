from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1GCEPersistentDiskVolumeSource",)


class V1GCEPersistentDiskVolumeSource(BaseModel):
    fs_type: str | None = Field(default_factory=lambda: None, alias="fsType")

    partition: int | None = Field(default_factory=lambda: None)

    pd_name: str | None = Field(default_factory=lambda: None, alias="pdName")

    read_only: bool | None = Field(default_factory=lambda: None, alias="readOnly")

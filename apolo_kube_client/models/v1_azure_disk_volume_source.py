from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1AzureDiskVolumeSource",)


class V1AzureDiskVolumeSource(BaseModel):
    caching_mode: str | None = Field(default_factory=lambda: None, alias="cachingMode")

    disk_name: str | None = Field(default_factory=lambda: None, alias="diskName")

    disk_uri: str | None = Field(default_factory=lambda: None, alias="diskURI")

    fs_type: str | None = Field(default_factory=lambda: None, alias="fsType")

    kind: str | None = Field(default_factory=lambda: None)

    read_only: bool | None = Field(default_factory=lambda: None, alias="readOnly")

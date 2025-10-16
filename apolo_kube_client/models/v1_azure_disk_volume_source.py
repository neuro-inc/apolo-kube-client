from __future__ import annotations

from pydantic import BaseModel, Field

__all__ = ("V1AzureDiskVolumeSource",)


class V1AzureDiskVolumeSource(BaseModel):
    caching_mode: str | None = Field(None, alias="cachingMode")

    disk_name: str | None = Field(None, alias="diskName")

    disk_uri: str | None = Field(None, alias="diskURI")

    fs_type: str | None = Field(None, alias="fsType")

    kind: str | None = Field(None, alias="kind")

    read_only: bool | None = Field(None, alias="readOnly")

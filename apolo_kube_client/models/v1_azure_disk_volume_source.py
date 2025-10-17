from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field


__all__ = ("V1AzureDiskVolumeSource",)


class V1AzureDiskVolumeSource(BaseModel):
    caching_mode: str | None = Field(
        default=None,
        serialization_alias="cachingMode",
        validation_alias=AliasChoices("caching_mode", "cachingMode"),
    )

    disk_name: str | None = Field(
        default=None,
        serialization_alias="diskName",
        validation_alias=AliasChoices("disk_name", "diskName"),
    )

    disk_uri: str | None = Field(
        default=None,
        serialization_alias="diskURI",
        validation_alias=AliasChoices("disk_uri", "diskURI"),
    )

    fs_type: str | None = Field(
        default=None,
        serialization_alias="fsType",
        validation_alias=AliasChoices("fs_type", "fsType"),
    )

    kind: str | None = Field(default=None)

    read_only: bool | None = Field(
        default=None,
        serialization_alias="readOnly",
        validation_alias=AliasChoices("read_only", "readOnly"),
    )

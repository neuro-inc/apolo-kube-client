from pydantic import AliasChoices, BaseModel, Field
from .utils import _exclude_if

__all__ = ("V1AzureDiskVolumeSource",)


class V1AzureDiskVolumeSource(BaseModel):
    caching_mode: str | None = Field(
        default=None,
        serialization_alias="cachingMode",
        validation_alias=AliasChoices("caching_mode", "cachingMode"),
        exclude_if=_exclude_if,
    )

    disk_name: str | None = Field(
        default=None,
        serialization_alias="diskName",
        validation_alias=AliasChoices("disk_name", "diskName"),
        exclude_if=_exclude_if,
    )

    disk_uri: str | None = Field(
        default=None,
        serialization_alias="diskURI",
        validation_alias=AliasChoices("disk_uri", "diskURI"),
        exclude_if=_exclude_if,
    )

    fs_type: str | None = Field(
        default=None,
        serialization_alias="fsType",
        validation_alias=AliasChoices("fs_type", "fsType"),
        exclude_if=_exclude_if,
    )

    kind: str | None = Field(default=None, exclude_if=_exclude_if)

    read_only: bool | None = Field(
        default=None,
        serialization_alias="readOnly",
        validation_alias=AliasChoices("read_only", "readOnly"),
        exclude_if=_exclude_if,
    )

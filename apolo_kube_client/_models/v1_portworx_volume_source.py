from pydantic import AliasChoices, BaseModel, Field
from .utils import _exclude_if

__all__ = ("V1PortworxVolumeSource",)


class V1PortworxVolumeSource(BaseModel):
    fs_type: str | None = Field(
        default=None,
        serialization_alias="fsType",
        validation_alias=AliasChoices("fs_type", "fsType"),
        exclude_if=_exclude_if,
    )

    read_only: bool | None = Field(
        default=None,
        serialization_alias="readOnly",
        validation_alias=AliasChoices("read_only", "readOnly"),
        exclude_if=_exclude_if,
    )

    volume_id: str | None = Field(
        default=None,
        serialization_alias="volumeID",
        validation_alias=AliasChoices("volume_id", "volumeID"),
        exclude_if=_exclude_if,
    )

from pydantic import AliasChoices, BaseModel, Field
from .utils import _exclude_if

__all__ = ("V1GCEPersistentDiskVolumeSource",)


class V1GCEPersistentDiskVolumeSource(BaseModel):
    fs_type: str | None = Field(
        default=None,
        serialization_alias="fsType",
        validation_alias=AliasChoices("fs_type", "fsType"),
        exclude_if=_exclude_if,
    )

    partition: int | None = Field(default=None, exclude_if=_exclude_if)

    pd_name: str | None = Field(
        default=None,
        serialization_alias="pdName",
        validation_alias=AliasChoices("pd_name", "pdName"),
        exclude_if=_exclude_if,
    )

    read_only: bool | None = Field(
        default=None,
        serialization_alias="readOnly",
        validation_alias=AliasChoices("read_only", "readOnly"),
        exclude_if=_exclude_if,
    )

from pydantic import AliasChoices, BaseModel, Field


__all__ = ("V1GCEPersistentDiskVolumeSource",)


class V1GCEPersistentDiskVolumeSource(BaseModel):
    fs_type: str | None = Field(
        default=None,
        serialization_alias="fsType",
        validation_alias=AliasChoices("fs_type", "fsType"),
    )

    partition: int | None = None

    pd_name: str | None = Field(
        default=None,
        serialization_alias="pdName",
        validation_alias=AliasChoices("pd_name", "pdName"),
    )

    read_only: bool | None = Field(
        default=None,
        serialization_alias="readOnly",
        validation_alias=AliasChoices("read_only", "readOnly"),
    )

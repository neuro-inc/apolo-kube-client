from pydantic import AliasChoices, BaseModel, Field


__all__ = ("V1AWSElasticBlockStoreVolumeSource",)


class V1AWSElasticBlockStoreVolumeSource(BaseModel):
    fs_type: str | None = Field(
        default=None,
        serialization_alias="fsType",
        validation_alias=AliasChoices("fs_type", "fsType"),
    )

    partition: int | None = None

    read_only: bool | None = Field(
        default=None,
        serialization_alias="readOnly",
        validation_alias=AliasChoices("read_only", "readOnly"),
    )

    volume_id: str | None = Field(
        default=None,
        serialization_alias="volumeID",
        validation_alias=AliasChoices("volume_id", "volumeID"),
    )

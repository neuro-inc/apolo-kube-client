from pydantic import AliasChoices, BaseModel, Field
from .v1_local_object_reference import V1LocalObjectReference

__all__ = ("V1CinderVolumeSource",)


class V1CinderVolumeSource(BaseModel):
    fs_type: str | None = Field(
        default=None,
        serialization_alias="fsType",
        validation_alias=AliasChoices("fs_type", "fsType"),
    )

    read_only: bool | None = Field(
        default=None,
        serialization_alias="readOnly",
        validation_alias=AliasChoices("read_only", "readOnly"),
    )

    secret_ref: V1LocalObjectReference = Field(
        default_factory=lambda: V1LocalObjectReference(),
        serialization_alias="secretRef",
        validation_alias=AliasChoices("secret_ref", "secretRef"),
    )

    volume_id: str | None = Field(
        default=None,
        serialization_alias="volumeID",
        validation_alias=AliasChoices("volume_id", "volumeID"),
    )

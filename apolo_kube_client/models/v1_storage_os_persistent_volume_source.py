from pydantic import AliasChoices, BaseModel, Field
from .v1_object_reference import V1ObjectReference

__all__ = ("V1StorageOSPersistentVolumeSource",)


class V1StorageOSPersistentVolumeSource(BaseModel):
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

    secret_ref: V1ObjectReference = Field(
        default_factory=lambda: V1ObjectReference(),
        serialization_alias="secretRef",
        validation_alias=AliasChoices("secret_ref", "secretRef"),
    )

    volume_name: str | None = Field(
        default=None,
        serialization_alias="volumeName",
        validation_alias=AliasChoices("volume_name", "volumeName"),
    )

    volume_namespace: str | None = Field(
        default=None,
        serialization_alias="volumeNamespace",
        validation_alias=AliasChoices("volume_namespace", "volumeNamespace"),
    )

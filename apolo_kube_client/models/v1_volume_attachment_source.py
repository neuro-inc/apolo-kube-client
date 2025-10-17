from pydantic import AliasChoices, BaseModel, Field
from .v1_persistent_volume_spec import V1PersistentVolumeSpec

__all__ = ("V1VolumeAttachmentSource",)


class V1VolumeAttachmentSource(BaseModel):
    inline_volume_spec: V1PersistentVolumeSpec = Field(
        default_factory=lambda: V1PersistentVolumeSpec(),
        serialization_alias="inlineVolumeSpec",
        validation_alias=AliasChoices("inline_volume_spec", "inlineVolumeSpec"),
    )

    persistent_volume_name: str | None = Field(
        default=None,
        serialization_alias="persistentVolumeName",
        validation_alias=AliasChoices("persistent_volume_name", "persistentVolumeName"),
    )

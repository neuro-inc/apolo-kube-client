from pydantic import AliasChoices, BaseModel, Field
from .v1_local_object_reference import V1LocalObjectReference

__all__ = ("V1CSIVolumeSource",)


class V1CSIVolumeSource(BaseModel):
    driver: str | None = None

    fs_type: str | None = Field(
        default=None,
        serialization_alias="fsType",
        validation_alias=AliasChoices("fs_type", "fsType"),
    )

    node_publish_secret_ref: V1LocalObjectReference = Field(
        default_factory=lambda: V1LocalObjectReference(),
        serialization_alias="nodePublishSecretRef",
        validation_alias=AliasChoices(
            "node_publish_secret_ref", "nodePublishSecretRef"
        ),
    )

    read_only: bool | None = Field(
        default=None,
        serialization_alias="readOnly",
        validation_alias=AliasChoices("read_only", "readOnly"),
    )

    volume_attributes: dict[str, str] = Field(
        default={},
        serialization_alias="volumeAttributes",
        validation_alias=AliasChoices("volume_attributes", "volumeAttributes"),
    )

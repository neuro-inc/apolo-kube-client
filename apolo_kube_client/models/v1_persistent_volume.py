from pydantic import AliasChoices, Field
from .base import ResourceModel
from .v1_object_meta import V1ObjectMeta
from .v1_persistent_volume_spec import V1PersistentVolumeSpec
from .v1_persistent_volume_status import V1PersistentVolumeStatus

__all__ = ("V1PersistentVolume",)


class V1PersistentVolume(ResourceModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    kind: str | None = None

    metadata: V1ObjectMeta = Field(default_factory=lambda: V1ObjectMeta())

    spec: V1PersistentVolumeSpec = Field(
        default_factory=lambda: V1PersistentVolumeSpec()
    )

    status: V1PersistentVolumeStatus = Field(
        default_factory=lambda: V1PersistentVolumeStatus()
    )

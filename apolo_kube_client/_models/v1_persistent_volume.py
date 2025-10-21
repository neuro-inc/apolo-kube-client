from pydantic import AliasChoices, Field
from .base import ResourceModel
from .base import _default_if_none
from .v1_object_meta import V1ObjectMeta
from .v1_persistent_volume_spec import V1PersistentVolumeSpec
from .v1_persistent_volume_status import V1PersistentVolumeStatus
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1PersistentVolume",)


class V1PersistentVolume(ResourceModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    kind: str | None = None

    metadata: Annotated[
        V1ObjectMeta, BeforeValidator(_default_if_none(V1ObjectMeta))
    ] = Field(default_factory=lambda: V1ObjectMeta())

    spec: Annotated[
        V1PersistentVolumeSpec,
        BeforeValidator(_default_if_none(V1PersistentVolumeSpec)),
    ] = Field(default_factory=lambda: V1PersistentVolumeSpec())

    status: Annotated[
        V1PersistentVolumeStatus,
        BeforeValidator(_default_if_none(V1PersistentVolumeStatus)),
    ] = Field(default_factory=lambda: V1PersistentVolumeStatus())

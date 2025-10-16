from __future__ import annotations

from pydantic import BaseModel, Field

from .v1_object_meta import V1ObjectMeta
from .v1_persistent_volume_spec import V1PersistentVolumeSpec
from .v1_persistent_volume_status import V1PersistentVolumeStatus

__all__ = ("V1PersistentVolume",)


class V1PersistentVolume(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ObjectMeta | None = Field(None, alias="metadata")

    spec: V1PersistentVolumeSpec | None = Field(None, alias="spec")

    status: V1PersistentVolumeStatus | None = Field(None, alias="status")

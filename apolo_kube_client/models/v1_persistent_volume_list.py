from __future__ import annotations

from pydantic import BaseModel, Field

from .v1_list_meta import V1ListMeta
from .v1_persistent_volume import V1PersistentVolume

__all__ = ("V1PersistentVolumeList",)


class V1PersistentVolumeList(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    items: list[V1PersistentVolume] | None = Field(None, alias="items")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ListMeta | None = Field(None, alias="metadata")

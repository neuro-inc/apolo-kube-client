from __future__ import annotations

from pydantic import BaseModel, Field

from .v1_csi_storage_capacity import V1CSIStorageCapacity
from .v1_list_meta import V1ListMeta

__all__ = ("V1CSIStorageCapacityList",)


class V1CSIStorageCapacityList(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    items: list[V1CSIStorageCapacity] | None = Field(None, alias="items")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ListMeta | None = Field(None, alias="metadata")

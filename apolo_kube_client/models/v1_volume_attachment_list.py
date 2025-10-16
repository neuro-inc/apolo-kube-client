from __future__ import annotations

from pydantic import BaseModel, Field

from .v1_list_meta import V1ListMeta
from .v1_volume_attachment import V1VolumeAttachment

__all__ = ("V1VolumeAttachmentList",)


class V1VolumeAttachmentList(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    items: list[V1VolumeAttachment] | None = Field(None, alias="items")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ListMeta | None = Field(None, alias="metadata")

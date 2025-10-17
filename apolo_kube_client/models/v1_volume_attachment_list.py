from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_list_meta import V1ListMeta
from .v1_volume_attachment import V1VolumeAttachment

__all__ = ("V1VolumeAttachmentList",)


class V1VolumeAttachmentList(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    items: list[V1VolumeAttachment] = Field(default=[])

    kind: str | None = Field(default=None)

    metadata: V1ListMeta

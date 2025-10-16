from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_volume_attachment_source import V1VolumeAttachmentSource

__all__ = ("V1VolumeAttachmentSpec",)


class V1VolumeAttachmentSpec(BaseModel):
    attacher: str | None = Field(default_factory=lambda: None, alias="attacher")

    node_name: str | None = Field(default_factory=lambda: None, alias="nodeName")

    source: V1VolumeAttachmentSource = Field(
        default_factory=lambda: V1VolumeAttachmentSource(), alias="source"
    )

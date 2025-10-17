from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_volume_attachment_source import V1VolumeAttachmentSource

__all__ = ("V1VolumeAttachmentSpec",)


class V1VolumeAttachmentSpec(BaseModel):
    attacher: str | None = Field(default=None)

    node_name: str | None = Field(
        default=None,
        serialization_alias="nodeName",
        validation_alias=AliasChoices("node_name", "nodeName"),
    )

    source: V1VolumeAttachmentSource = Field(
        default_factory=lambda: V1VolumeAttachmentSource()
    )

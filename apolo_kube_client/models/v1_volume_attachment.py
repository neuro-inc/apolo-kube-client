from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_object_meta import V1ObjectMeta
from .v1_volume_attachment_spec import V1VolumeAttachmentSpec
from .v1_volume_attachment_status import V1VolumeAttachmentStatus

__all__ = ("V1VolumeAttachment",)


class V1VolumeAttachment(BaseModel):
    api_version: str | None = Field(default_factory=lambda: None, alias="apiVersion")

    kind: str | None = Field(default_factory=lambda: None, alias="kind")

    metadata: V1ObjectMeta = Field(
        default_factory=lambda: V1ObjectMeta(), alias="metadata"
    )

    spec: V1VolumeAttachmentSpec = Field(
        default_factory=lambda: V1VolumeAttachmentSpec(), alias="spec"
    )

    status: V1VolumeAttachmentStatus = Field(
        default_factory=lambda: V1VolumeAttachmentStatus(), alias="status"
    )

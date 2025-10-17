from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_volume_error import V1VolumeError

__all__ = ("V1VolumeAttachmentStatus",)


class V1VolumeAttachmentStatus(BaseModel):
    attach_error: V1VolumeError = Field(
        default_factory=lambda: V1VolumeError(), alias="attachError"
    )

    attached: bool | None = Field(default_factory=lambda: None)

    attachment_metadata: dict[str, str] = Field(
        default_factory=lambda: {}, alias="attachmentMetadata"
    )

    detach_error: V1VolumeError = Field(
        default_factory=lambda: V1VolumeError(), alias="detachError"
    )

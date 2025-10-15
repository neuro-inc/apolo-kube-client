from pydantic import BaseModel, Field

from .v1_volume_error import V1VolumeError


class V1VolumeAttachmentStatus(BaseModel):
    attach_error: V1VolumeError | None = Field(None, alias="attachError")

    attached: bool | None = Field(None, alias="attached")

    attachment_metadata: dict(str, str) | None = Field(None, alias="attachmentMetadata")

    detach_error: V1VolumeError | None = Field(None, alias="detachError")

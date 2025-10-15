from pydantic import BaseModel, Field

from .v1_object_meta import V1ObjectMeta
from .v1_volume_attachment_spec import V1VolumeAttachmentSpec
from .v1_volume_attachment_status import V1VolumeAttachmentStatus


class V1VolumeAttachment(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ObjectMeta | None = Field(None, alias="metadata")

    spec: V1VolumeAttachmentSpec | None = Field(None, alias="spec")

    status: V1VolumeAttachmentStatus | None = Field(None, alias="status")

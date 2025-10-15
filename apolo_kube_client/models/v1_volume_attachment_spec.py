from pydantic import BaseModel, Field

from .v1_volume_attachment_source import V1VolumeAttachmentSource


class V1VolumeAttachmentSpec(BaseModel):
    attacher: str | None = Field(None, alias="attacher")

    node_name: str | None = Field(None, alias="nodeName")

    source: V1VolumeAttachmentSource | None = Field(None, alias="source")

from pydantic import AliasChoices, BaseModel, Field
from .utils import _default_if_none
from .v1_volume_attachment_source import V1VolumeAttachmentSource
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1VolumeAttachmentSpec",)


class V1VolumeAttachmentSpec(BaseModel):
    attacher: str | None = None

    node_name: str | None = Field(
        default=None,
        serialization_alias="nodeName",
        validation_alias=AliasChoices("node_name", "nodeName"),
    )

    source: Annotated[
        V1VolumeAttachmentSource,
        BeforeValidator(_default_if_none(V1VolumeAttachmentSource)),
    ] = Field(default_factory=lambda: V1VolumeAttachmentSource())

from pydantic import AliasChoices, BaseModel, Field
from .utils import _default_if_none
from .utils import _exclude_if
from .v1_volume_attachment_source import V1VolumeAttachmentSource
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1VolumeAttachmentSpec",)


class V1VolumeAttachmentSpec(BaseModel):
    attacher: str | None = Field(default=None, exclude_if=_exclude_if)

    node_name: str | None = Field(
        default=None,
        serialization_alias="nodeName",
        validation_alias=AliasChoices("node_name", "nodeName"),
        exclude_if=_exclude_if,
    )

    source: Annotated[
        V1VolumeAttachmentSource,
        BeforeValidator(_default_if_none(V1VolumeAttachmentSource)),
    ] = Field(
        default_factory=lambda: V1VolumeAttachmentSource(), exclude_if=_exclude_if
    )

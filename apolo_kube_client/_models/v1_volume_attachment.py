from pydantic import AliasChoices, Field
from .base import ResourceModel
from .utils import _default_if_none
from .v1_object_meta import V1ObjectMeta
from .v1_volume_attachment_spec import V1VolumeAttachmentSpec
from .v1_volume_attachment_status import V1VolumeAttachmentStatus
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1VolumeAttachment",)


class V1VolumeAttachment(ResourceModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    kind: str | None = None

    metadata: Annotated[
        V1ObjectMeta, BeforeValidator(_default_if_none(V1ObjectMeta))
    ] = Field(default_factory=lambda: V1ObjectMeta())

    spec: Annotated[
        V1VolumeAttachmentSpec,
        BeforeValidator(_default_if_none(V1VolumeAttachmentSpec)),
    ] = Field(default_factory=lambda: V1VolumeAttachmentSpec())

    status: Annotated[
        V1VolumeAttachmentStatus,
        BeforeValidator(_default_if_none(V1VolumeAttachmentStatus)),
    ] = Field(default_factory=lambda: V1VolumeAttachmentStatus())

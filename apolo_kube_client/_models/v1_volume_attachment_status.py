from typing import Annotated, ClassVar, Final

from pydantic import BeforeValidator, Field

from .base_model import BaseConfiguredModel
from .utils import _collection_if_none, _default_if_none
from .v1_volume_error import V1VolumeError


__all__ = ("V1VolumeAttachmentStatus",)


class V1VolumeAttachmentStatus(BaseConfiguredModel):
    """VolumeAttachmentStatus is the status of a VolumeAttachment request."""

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.storage.v1.VolumeAttachmentStatus"
    )

    attach_error: Annotated[
        V1VolumeError,
        Field(
            alias="attachError",
            description="""attachError represents the last error encountered during attach operation, if any. This field must only be set by the entity completing the attach operation, i.e. the external-attacher.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1VolumeError)),
    ] = V1VolumeError()

    attached: Annotated[
        bool,
        Field(
            description="""attached indicates the volume is successfully attached. This field must only be set by the entity completing the attach operation, i.e. the external-attacher."""
        ),
    ]

    attachment_metadata: Annotated[
        dict[str, str],
        Field(
            alias="attachmentMetadata",
            description="""attachmentMetadata is populated with any information returned by the attach operation, upon successful attach, that must be passed into subsequent WaitForAttach or Mount calls. This field must only be set by the entity completing the attach operation, i.e. the external-attacher.""",
            exclude_if=lambda v: v == {},
        ),
        BeforeValidator(_collection_if_none("{}")),
    ] = {}

    detach_error: Annotated[
        V1VolumeError,
        Field(
            alias="detachError",
            description="""detachError represents the last error encountered during detach operation, if any. This field must only be set by the entity completing the detach operation, i.e. the external-attacher.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1VolumeError)),
    ] = V1VolumeError()

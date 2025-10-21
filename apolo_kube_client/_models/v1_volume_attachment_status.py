from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .utils import _default_if_none
from .v1_volume_error import V1VolumeError
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1VolumeAttachmentStatus",)


class V1VolumeAttachmentStatus(BaseModel):
    attach_error: Annotated[
        V1VolumeError, BeforeValidator(_default_if_none(V1VolumeError))
    ] = Field(
        default_factory=lambda: V1VolumeError(),
        serialization_alias="attachError",
        validation_alias=AliasChoices("attach_error", "attachError"),
    )

    attached: bool | None = None

    attachment_metadata: Annotated[
        dict[str, str], BeforeValidator(_collection_if_none("{}"))
    ] = Field(
        default={},
        serialization_alias="attachmentMetadata",
        validation_alias=AliasChoices("attachment_metadata", "attachmentMetadata"),
    )

    detach_error: Annotated[
        V1VolumeError, BeforeValidator(_default_if_none(V1VolumeError))
    ] = Field(
        default_factory=lambda: V1VolumeError(),
        serialization_alias="detachError",
        validation_alias=AliasChoices("detach_error", "detachError"),
    )

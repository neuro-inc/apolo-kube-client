from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .utils import _default_if_none
from .utils import _exclude_if
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
        exclude_if=_exclude_if,
    )

    attached: bool | None = Field(default=None, exclude_if=_exclude_if)

    attachment_metadata: Annotated[
        dict[str, str], BeforeValidator(_collection_if_none("{}"))
    ] = Field(
        default={},
        serialization_alias="attachmentMetadata",
        validation_alias=AliasChoices("attachment_metadata", "attachmentMetadata"),
        exclude_if=_exclude_if,
    )

    detach_error: Annotated[
        V1VolumeError, BeforeValidator(_default_if_none(V1VolumeError))
    ] = Field(
        default_factory=lambda: V1VolumeError(),
        serialization_alias="detachError",
        validation_alias=AliasChoices("detach_error", "detachError"),
        exclude_if=_exclude_if,
    )

from pydantic import AliasChoices, BaseModel, Field
from .utils import _default_if_none
from .v1_persistent_volume_spec import V1PersistentVolumeSpec
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1VolumeAttachmentSource",)


class V1VolumeAttachmentSource(BaseModel):
    inline_volume_spec: Annotated[
        V1PersistentVolumeSpec,
        BeforeValidator(_default_if_none(V1PersistentVolumeSpec)),
    ] = Field(
        default_factory=lambda: V1PersistentVolumeSpec(),
        serialization_alias="inlineVolumeSpec",
        validation_alias=AliasChoices("inline_volume_spec", "inlineVolumeSpec"),
    )

    persistent_volume_name: str | None = Field(
        default=None,
        serialization_alias="persistentVolumeName",
        validation_alias=AliasChoices("persistent_volume_name", "persistentVolumeName"),
    )

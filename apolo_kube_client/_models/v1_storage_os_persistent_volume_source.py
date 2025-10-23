from pydantic import AliasChoices, BaseModel, Field
from .utils import _default_if_none
from .utils import _exclude_if
from .v1_object_reference import V1ObjectReference
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1StorageOSPersistentVolumeSource",)


class V1StorageOSPersistentVolumeSource(BaseModel):
    fs_type: str | None = Field(
        default=None,
        serialization_alias="fsType",
        validation_alias=AliasChoices("fs_type", "fsType"),
        exclude_if=_exclude_if,
    )

    read_only: bool | None = Field(
        default=None,
        serialization_alias="readOnly",
        validation_alias=AliasChoices("read_only", "readOnly"),
        exclude_if=_exclude_if,
    )

    secret_ref: Annotated[
        V1ObjectReference, BeforeValidator(_default_if_none(V1ObjectReference))
    ] = Field(
        default_factory=lambda: V1ObjectReference(),
        serialization_alias="secretRef",
        validation_alias=AliasChoices("secret_ref", "secretRef"),
        exclude_if=_exclude_if,
    )

    volume_name: str | None = Field(
        default=None,
        serialization_alias="volumeName",
        validation_alias=AliasChoices("volume_name", "volumeName"),
        exclude_if=_exclude_if,
    )

    volume_namespace: str | None = Field(
        default=None,
        serialization_alias="volumeNamespace",
        validation_alias=AliasChoices("volume_namespace", "volumeNamespace"),
        exclude_if=_exclude_if,
    )

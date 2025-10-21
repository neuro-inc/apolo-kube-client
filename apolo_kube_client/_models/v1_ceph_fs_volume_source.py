from pydantic import AliasChoices, BaseModel, Field
from .base import _default_if_none
from .v1_local_object_reference import V1LocalObjectReference
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1CephFSVolumeSource",)


class V1CephFSVolumeSource(BaseModel):
    monitors: list[str] = []

    path: str | None = None

    read_only: bool | None = Field(
        default=None,
        serialization_alias="readOnly",
        validation_alias=AliasChoices("read_only", "readOnly"),
    )

    secret_file: str | None = Field(
        default=None,
        serialization_alias="secretFile",
        validation_alias=AliasChoices("secret_file", "secretFile"),
    )

    secret_ref: Annotated[
        V1LocalObjectReference,
        BeforeValidator(_default_if_none(V1LocalObjectReference)),
    ] = Field(
        default_factory=lambda: V1LocalObjectReference(),
        serialization_alias="secretRef",
        validation_alias=AliasChoices("secret_ref", "secretRef"),
    )

    user: str | None = None

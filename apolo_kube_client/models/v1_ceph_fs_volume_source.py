from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_local_object_reference import V1LocalObjectReference

__all__ = ("V1CephFSVolumeSource",)


class V1CephFSVolumeSource(BaseModel):
    monitors: list[str] = Field(default=[])

    path: str | None = Field(default=None)

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

    secret_ref: V1LocalObjectReference = Field(
        default_factory=lambda: V1LocalObjectReference(),
        serialization_alias="secretRef",
        validation_alias=AliasChoices("secret_ref", "secretRef"),
    )

    user: str | None = Field(default=None)

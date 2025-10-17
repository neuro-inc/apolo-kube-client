from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_local_object_reference import V1LocalObjectReference

__all__ = ("V1CephFSVolumeSource",)


class V1CephFSVolumeSource(BaseModel):
    monitors: list[str] = Field(default_factory=lambda: [])

    path: str | None = Field(default_factory=lambda: None)

    read_only: bool | None = Field(default_factory=lambda: None, alias="readOnly")

    secret_file: str | None = Field(default_factory=lambda: None, alias="secretFile")

    secret_ref: V1LocalObjectReference = Field(
        default_factory=lambda: V1LocalObjectReference(), alias="secretRef"
    )

    user: str | None = Field(default_factory=lambda: None)

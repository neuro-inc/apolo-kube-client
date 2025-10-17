from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_local_object_reference import V1LocalObjectReference

__all__ = ("V1RBDVolumeSource",)


class V1RBDVolumeSource(BaseModel):
    fs_type: str | None = Field(default_factory=lambda: None, alias="fsType")

    image: str | None = Field(default_factory=lambda: None)

    keyring: str | None = Field(default_factory=lambda: None)

    monitors: list[str] = Field(default_factory=lambda: [])

    pool: str | None = Field(default_factory=lambda: None)

    read_only: bool | None = Field(default_factory=lambda: None, alias="readOnly")

    secret_ref: V1LocalObjectReference = Field(
        default_factory=lambda: V1LocalObjectReference(), alias="secretRef"
    )

    user: str | None = Field(default_factory=lambda: None)

from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_secret_reference import V1SecretReference

__all__ = ("V1CinderPersistentVolumeSource",)


class V1CinderPersistentVolumeSource(BaseModel):
    fs_type: str | None = Field(default_factory=lambda: None, alias="fsType")

    read_only: bool | None = Field(default_factory=lambda: None, alias="readOnly")

    secret_ref: V1SecretReference = Field(
        default_factory=lambda: V1SecretReference(), alias="secretRef"
    )

    volume_id: str | None = Field(default_factory=lambda: None, alias="volumeID")

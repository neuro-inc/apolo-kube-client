from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_secret_reference import V1SecretReference

__all__ = ("V1CephFSPersistentVolumeSource",)


class V1CephFSPersistentVolumeSource(BaseModel):
    monitors: list[str] = Field(default_factory=lambda: [])

    path: str | None = Field(default_factory=lambda: None)

    read_only: bool | None = Field(default_factory=lambda: None, alias="readOnly")

    secret_file: str | None = Field(default_factory=lambda: None, alias="secretFile")

    secret_ref: V1SecretReference = Field(
        default_factory=lambda: V1SecretReference(), alias="secretRef"
    )

    user: str | None = Field(default_factory=lambda: None)

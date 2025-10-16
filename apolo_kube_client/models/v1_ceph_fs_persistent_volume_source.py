from __future__ import annotations

from pydantic import BaseModel, Field

from .v1_secret_reference import V1SecretReference

__all__ = ("V1CephFSPersistentVolumeSource",)


class V1CephFSPersistentVolumeSource(BaseModel):
    monitors: list[str] | None = Field(None, alias="monitors")

    path: str | None = Field(None, alias="path")

    read_only: bool | None = Field(None, alias="readOnly")

    secret_file: str | None = Field(None, alias="secretFile")

    secret_ref: V1SecretReference | None = Field(None, alias="secretRef")

    user: str | None = Field(None, alias="user")

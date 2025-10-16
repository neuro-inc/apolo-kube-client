from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_secret_reference import V1SecretReference

__all__ = ("V1RBDPersistentVolumeSource",)


class V1RBDPersistentVolumeSource(BaseModel):
    fs_type: str | None = Field(default_factory=lambda: None, alias="fsType")

    image: str | None = Field(default_factory=lambda: None, alias="image")

    keyring: str | None = Field(default_factory=lambda: None, alias="keyring")

    monitors: list[str] = Field(default_factory=lambda: [], alias="monitors")

    pool: str | None = Field(default_factory=lambda: None, alias="pool")

    read_only: bool | None = Field(default_factory=lambda: None, alias="readOnly")

    secret_ref: V1SecretReference = Field(
        default_factory=lambda: V1SecretReference(), alias="secretRef"
    )

    user: str | None = Field(default_factory=lambda: None, alias="user")

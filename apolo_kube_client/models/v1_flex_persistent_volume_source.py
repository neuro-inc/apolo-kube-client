from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_secret_reference import V1SecretReference

__all__ = ("V1FlexPersistentVolumeSource",)


class V1FlexPersistentVolumeSource(BaseModel):
    driver: str | None = Field(default_factory=lambda: None, alias="driver")

    fs_type: str | None = Field(default_factory=lambda: None, alias="fsType")

    options: dict[str, str] = Field(default_factory=lambda: {}, alias="options")

    read_only: bool | None = Field(default_factory=lambda: None, alias="readOnly")

    secret_ref: V1SecretReference = Field(
        default_factory=lambda: V1SecretReference(), alias="secretRef"
    )

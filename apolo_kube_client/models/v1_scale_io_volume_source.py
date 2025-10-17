from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_local_object_reference import V1LocalObjectReference

__all__ = ("V1ScaleIOVolumeSource",)


class V1ScaleIOVolumeSource(BaseModel):
    fs_type: str | None = Field(default_factory=lambda: None, alias="fsType")

    gateway: str | None = Field(default_factory=lambda: None)

    protection_domain: str | None = Field(
        default_factory=lambda: None, alias="protectionDomain"
    )

    read_only: bool | None = Field(default_factory=lambda: None, alias="readOnly")

    secret_ref: V1LocalObjectReference = Field(
        default_factory=lambda: V1LocalObjectReference(), alias="secretRef"
    )

    ssl_enabled: bool | None = Field(default_factory=lambda: None, alias="sslEnabled")

    storage_mode: str | None = Field(default_factory=lambda: None, alias="storageMode")

    storage_pool: str | None = Field(default_factory=lambda: None, alias="storagePool")

    system: str | None = Field(default_factory=lambda: None)

    volume_name: str | None = Field(default_factory=lambda: None, alias="volumeName")

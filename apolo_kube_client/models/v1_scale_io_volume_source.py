from __future__ import annotations

from pydantic import BaseModel, Field

from .v1_local_object_reference import V1LocalObjectReference

__all__ = ("V1ScaleIOVolumeSource",)


class V1ScaleIOVolumeSource(BaseModel):
    fs_type: str | None = Field(None, alias="fsType")

    gateway: str | None = Field(None, alias="gateway")

    protection_domain: str | None = Field(None, alias="protectionDomain")

    read_only: bool | None = Field(None, alias="readOnly")

    secret_ref: V1LocalObjectReference | None = Field(None, alias="secretRef")

    ssl_enabled: bool | None = Field(None, alias="sslEnabled")

    storage_mode: str | None = Field(None, alias="storageMode")

    storage_pool: str | None = Field(None, alias="storagePool")

    system: str | None = Field(None, alias="system")

    volume_name: str | None = Field(None, alias="volumeName")

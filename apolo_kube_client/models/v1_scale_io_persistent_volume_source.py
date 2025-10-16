from __future__ import annotations

from pydantic import BaseModel, Field

from .v1_secret_reference import V1SecretReference

__all__ = ("V1ScaleIOPersistentVolumeSource",)


class V1ScaleIOPersistentVolumeSource(BaseModel):
    fs_type: str | None = Field(None, alias="fsType")

    gateway: str | None = Field(None, alias="gateway")

    protection_domain: str | None = Field(None, alias="protectionDomain")

    read_only: bool | None = Field(None, alias="readOnly")

    secret_ref: V1SecretReference | None = Field(None, alias="secretRef")

    ssl_enabled: bool | None = Field(None, alias="sslEnabled")

    storage_mode: str | None = Field(None, alias="storageMode")

    storage_pool: str | None = Field(None, alias="storagePool")

    system: str | None = Field(None, alias="system")

    volume_name: str | None = Field(None, alias="volumeName")

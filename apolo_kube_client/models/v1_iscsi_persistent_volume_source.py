from __future__ import annotations

from pydantic import BaseModel, Field

from .v1_secret_reference import V1SecretReference

__all__ = ("V1ISCSIPersistentVolumeSource",)


class V1ISCSIPersistentVolumeSource(BaseModel):
    chap_auth_discovery: bool | None = Field(None, alias="chapAuthDiscovery")

    chap_auth_session: bool | None = Field(None, alias="chapAuthSession")

    fs_type: str | None = Field(None, alias="fsType")

    initiator_name: str | None = Field(None, alias="initiatorName")

    iqn: str | None = Field(None, alias="iqn")

    iscsi_interface: str | None = Field(None, alias="iscsiInterface")

    lun: int | None = Field(None, alias="lun")

    portals: list[str] | None = Field(None, alias="portals")

    read_only: bool | None = Field(None, alias="readOnly")

    secret_ref: V1SecretReference | None = Field(None, alias="secretRef")

    target_portal: str | None = Field(None, alias="targetPortal")

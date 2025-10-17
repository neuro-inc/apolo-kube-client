from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_secret_reference import V1SecretReference

__all__ = ("V1ISCSIPersistentVolumeSource",)


class V1ISCSIPersistentVolumeSource(BaseModel):
    chap_auth_discovery: bool | None = Field(
        default_factory=lambda: None, alias="chapAuthDiscovery"
    )

    chap_auth_session: bool | None = Field(
        default_factory=lambda: None, alias="chapAuthSession"
    )

    fs_type: str | None = Field(default_factory=lambda: None, alias="fsType")

    initiator_name: str | None = Field(
        default_factory=lambda: None, alias="initiatorName"
    )

    iqn: str | None = Field(default_factory=lambda: None)

    iscsi_interface: str | None = Field(
        default_factory=lambda: None, alias="iscsiInterface"
    )

    lun: int | None = Field(default_factory=lambda: None)

    portals: list[str] = Field(default_factory=lambda: [])

    read_only: bool | None = Field(default_factory=lambda: None, alias="readOnly")

    secret_ref: V1SecretReference = Field(
        default_factory=lambda: V1SecretReference(), alias="secretRef"
    )

    target_portal: str | None = Field(
        default_factory=lambda: None, alias="targetPortal"
    )

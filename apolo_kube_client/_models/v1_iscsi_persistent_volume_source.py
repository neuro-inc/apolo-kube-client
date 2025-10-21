from pydantic import AliasChoices, BaseModel, Field
from .base import _default_if_none
from .v1_secret_reference import V1SecretReference
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1ISCSIPersistentVolumeSource",)


class V1ISCSIPersistentVolumeSource(BaseModel):
    chap_auth_discovery: bool | None = Field(
        default=None,
        serialization_alias="chapAuthDiscovery",
        validation_alias=AliasChoices("chap_auth_discovery", "chapAuthDiscovery"),
    )

    chap_auth_session: bool | None = Field(
        default=None,
        serialization_alias="chapAuthSession",
        validation_alias=AliasChoices("chap_auth_session", "chapAuthSession"),
    )

    fs_type: str | None = Field(
        default=None,
        serialization_alias="fsType",
        validation_alias=AliasChoices("fs_type", "fsType"),
    )

    initiator_name: str | None = Field(
        default=None,
        serialization_alias="initiatorName",
        validation_alias=AliasChoices("initiator_name", "initiatorName"),
    )

    iqn: str | None = None

    iscsi_interface: str | None = Field(
        default=None,
        serialization_alias="iscsiInterface",
        validation_alias=AliasChoices("iscsi_interface", "iscsiInterface"),
    )

    lun: int | None = None

    portals: list[str] = []

    read_only: bool | None = Field(
        default=None,
        serialization_alias="readOnly",
        validation_alias=AliasChoices("read_only", "readOnly"),
    )

    secret_ref: Annotated[
        V1SecretReference, BeforeValidator(_default_if_none(V1SecretReference))
    ] = Field(
        default_factory=lambda: V1SecretReference(),
        serialization_alias="secretRef",
        validation_alias=AliasChoices("secret_ref", "secretRef"),
    )

    target_portal: str | None = Field(
        default=None,
        serialization_alias="targetPortal",
        validation_alias=AliasChoices("target_portal", "targetPortal"),
    )

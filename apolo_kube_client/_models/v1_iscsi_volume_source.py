from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .utils import _default_if_none
from .utils import _exclude_if
from .v1_local_object_reference import V1LocalObjectReference
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1ISCSIVolumeSource",)


class V1ISCSIVolumeSource(BaseModel):
    chap_auth_discovery: bool | None = Field(
        default=None,
        serialization_alias="chapAuthDiscovery",
        validation_alias=AliasChoices("chap_auth_discovery", "chapAuthDiscovery"),
        exclude_if=_exclude_if,
    )

    chap_auth_session: bool | None = Field(
        default=None,
        serialization_alias="chapAuthSession",
        validation_alias=AliasChoices("chap_auth_session", "chapAuthSession"),
        exclude_if=_exclude_if,
    )

    fs_type: str | None = Field(
        default=None,
        serialization_alias="fsType",
        validation_alias=AliasChoices("fs_type", "fsType"),
        exclude_if=_exclude_if,
    )

    initiator_name: str | None = Field(
        default=None,
        serialization_alias="initiatorName",
        validation_alias=AliasChoices("initiator_name", "initiatorName"),
        exclude_if=_exclude_if,
    )

    iqn: str | None = Field(default=None, exclude_if=_exclude_if)

    iscsi_interface: str | None = Field(
        default=None,
        serialization_alias="iscsiInterface",
        validation_alias=AliasChoices("iscsi_interface", "iscsiInterface"),
        exclude_if=_exclude_if,
    )

    lun: int | None = Field(default=None, exclude_if=_exclude_if)

    portals: Annotated[list[str], BeforeValidator(_collection_if_none("[]"))] = Field(
        default=[], exclude_if=_exclude_if
    )

    read_only: bool | None = Field(
        default=None,
        serialization_alias="readOnly",
        validation_alias=AliasChoices("read_only", "readOnly"),
        exclude_if=_exclude_if,
    )

    secret_ref: Annotated[
        V1LocalObjectReference,
        BeforeValidator(_default_if_none(V1LocalObjectReference)),
    ] = Field(
        default_factory=lambda: V1LocalObjectReference(),
        serialization_alias="secretRef",
        validation_alias=AliasChoices("secret_ref", "secretRef"),
        exclude_if=_exclude_if,
    )

    target_portal: str | None = Field(
        default=None,
        serialization_alias="targetPortal",
        validation_alias=AliasChoices("target_portal", "targetPortal"),
        exclude_if=_exclude_if,
    )

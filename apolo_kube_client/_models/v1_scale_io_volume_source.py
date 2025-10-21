from pydantic import AliasChoices, BaseModel, Field
from .utils import _default_if_none
from .v1_local_object_reference import V1LocalObjectReference
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1ScaleIOVolumeSource",)


class V1ScaleIOVolumeSource(BaseModel):
    fs_type: str | None = Field(
        default=None,
        serialization_alias="fsType",
        validation_alias=AliasChoices("fs_type", "fsType"),
    )

    gateway: str | None = None

    protection_domain: str | None = Field(
        default=None,
        serialization_alias="protectionDomain",
        validation_alias=AliasChoices("protection_domain", "protectionDomain"),
    )

    read_only: bool | None = Field(
        default=None,
        serialization_alias="readOnly",
        validation_alias=AliasChoices("read_only", "readOnly"),
    )

    secret_ref: Annotated[
        V1LocalObjectReference,
        BeforeValidator(_default_if_none(V1LocalObjectReference)),
    ] = Field(
        default_factory=lambda: V1LocalObjectReference(),
        serialization_alias="secretRef",
        validation_alias=AliasChoices("secret_ref", "secretRef"),
    )

    ssl_enabled: bool | None = Field(
        default=None,
        serialization_alias="sslEnabled",
        validation_alias=AliasChoices("ssl_enabled", "sslEnabled"),
    )

    storage_mode: str | None = Field(
        default=None,
        serialization_alias="storageMode",
        validation_alias=AliasChoices("storage_mode", "storageMode"),
    )

    storage_pool: str | None = Field(
        default=None,
        serialization_alias="storagePool",
        validation_alias=AliasChoices("storage_pool", "storagePool"),
    )

    system: str | None = None

    volume_name: str | None = Field(
        default=None,
        serialization_alias="volumeName",
        validation_alias=AliasChoices("volume_name", "volumeName"),
    )

from pydantic import AliasChoices, BaseModel, Field
from .utils import _default_if_none
from .utils import _exclude_if
from .v1_secret_reference import V1SecretReference
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1ScaleIOPersistentVolumeSource",)


class V1ScaleIOPersistentVolumeSource(BaseModel):
    fs_type: str | None = Field(
        default=None,
        serialization_alias="fsType",
        validation_alias=AliasChoices("fs_type", "fsType"),
        exclude_if=_exclude_if,
    )

    gateway: str | None = Field(default=None, exclude_if=_exclude_if)

    protection_domain: str | None = Field(
        default=None,
        serialization_alias="protectionDomain",
        validation_alias=AliasChoices("protection_domain", "protectionDomain"),
        exclude_if=_exclude_if,
    )

    read_only: bool | None = Field(
        default=None,
        serialization_alias="readOnly",
        validation_alias=AliasChoices("read_only", "readOnly"),
        exclude_if=_exclude_if,
    )

    secret_ref: Annotated[
        V1SecretReference, BeforeValidator(_default_if_none(V1SecretReference))
    ] = Field(
        default_factory=lambda: V1SecretReference(),
        serialization_alias="secretRef",
        validation_alias=AliasChoices("secret_ref", "secretRef"),
        exclude_if=_exclude_if,
    )

    ssl_enabled: bool | None = Field(
        default=None,
        serialization_alias="sslEnabled",
        validation_alias=AliasChoices("ssl_enabled", "sslEnabled"),
        exclude_if=_exclude_if,
    )

    storage_mode: str | None = Field(
        default=None,
        serialization_alias="storageMode",
        validation_alias=AliasChoices("storage_mode", "storageMode"),
        exclude_if=_exclude_if,
    )

    storage_pool: str | None = Field(
        default=None,
        serialization_alias="storagePool",
        validation_alias=AliasChoices("storage_pool", "storagePool"),
        exclude_if=_exclude_if,
    )

    system: str | None = Field(default=None, exclude_if=_exclude_if)

    volume_name: str | None = Field(
        default=None,
        serialization_alias="volumeName",
        validation_alias=AliasChoices("volume_name", "volumeName"),
        exclude_if=_exclude_if,
    )

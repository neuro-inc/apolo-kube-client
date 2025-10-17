from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_secret_reference import V1SecretReference

__all__ = ("V1RBDPersistentVolumeSource",)


class V1RBDPersistentVolumeSource(BaseModel):
    fs_type: str | None = Field(
        default=None,
        serialization_alias="fsType",
        validation_alias=AliasChoices("fs_type", "fsType"),
    )

    image: str | None = Field(default=None)

    keyring: str | None = Field(default=None)

    monitors: list[str] = Field(default=[])

    pool: str | None = Field(default=None)

    read_only: bool | None = Field(
        default=None,
        serialization_alias="readOnly",
        validation_alias=AliasChoices("read_only", "readOnly"),
    )

    secret_ref: V1SecretReference = Field(
        default_factory=lambda: V1SecretReference(),
        serialization_alias="secretRef",
        validation_alias=AliasChoices("secret_ref", "secretRef"),
    )

    user: str | None = Field(default=None)

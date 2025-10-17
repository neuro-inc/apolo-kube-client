from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_secret_reference import V1SecretReference

__all__ = ("V1FlexPersistentVolumeSource",)


class V1FlexPersistentVolumeSource(BaseModel):
    driver: str | None = Field(default=None)

    fs_type: str | None = Field(
        default=None,
        serialization_alias="fsType",
        validation_alias=AliasChoices("fs_type", "fsType"),
    )

    options: dict[str, str] = Field(default={})

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

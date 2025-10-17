from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field


__all__ = ("V1AzureFilePersistentVolumeSource",)


class V1AzureFilePersistentVolumeSource(BaseModel):
    read_only: bool | None = Field(
        default=None,
        serialization_alias="readOnly",
        validation_alias=AliasChoices("read_only", "readOnly"),
    )

    secret_name: str | None = Field(
        default=None,
        serialization_alias="secretName",
        validation_alias=AliasChoices("secret_name", "secretName"),
    )

    secret_namespace: str | None = Field(
        default=None,
        serialization_alias="secretNamespace",
        validation_alias=AliasChoices("secret_namespace", "secretNamespace"),
    )

    share_name: str | None = Field(
        default=None,
        serialization_alias="shareName",
        validation_alias=AliasChoices("share_name", "shareName"),
    )

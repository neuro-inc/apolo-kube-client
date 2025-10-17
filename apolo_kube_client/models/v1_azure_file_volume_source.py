from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field


__all__ = ("V1AzureFileVolumeSource",)


class V1AzureFileVolumeSource(BaseModel):
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

    share_name: str | None = Field(
        default=None,
        serialization_alias="shareName",
        validation_alias=AliasChoices("share_name", "shareName"),
    )

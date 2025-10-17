from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1AzureFilePersistentVolumeSource",)


class V1AzureFilePersistentVolumeSource(BaseModel):
    read_only: bool | None = Field(default_factory=lambda: None, alias="readOnly")

    secret_name: str | None = Field(default_factory=lambda: None, alias="secretName")

    secret_namespace: str | None = Field(
        default_factory=lambda: None, alias="secretNamespace"
    )

    share_name: str | None = Field(default_factory=lambda: None, alias="shareName")

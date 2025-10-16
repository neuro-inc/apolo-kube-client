from __future__ import annotations

from pydantic import BaseModel, Field

__all__ = ("V1AzureFilePersistentVolumeSource",)


class V1AzureFilePersistentVolumeSource(BaseModel):
    read_only: bool | None = Field(None, alias="readOnly")

    secret_name: str | None = Field(None, alias="secretName")

    secret_namespace: str | None = Field(None, alias="secretNamespace")

    share_name: str | None = Field(None, alias="shareName")

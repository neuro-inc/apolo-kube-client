from __future__ import annotations

from pydantic import BaseModel, Field

__all__ = ("V1AzureFileVolumeSource",)


class V1AzureFileVolumeSource(BaseModel):
    read_only: bool | None = Field(None, alias="readOnly")

    secret_name: str | None = Field(None, alias="secretName")

    share_name: str | None = Field(None, alias="shareName")

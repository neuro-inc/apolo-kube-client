from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1AzureFileVolumeSource",)


class V1AzureFileVolumeSource(BaseModel):
    read_only: bool | None = Field(default_factory=lambda: None, alias="readOnly")

    secret_name: str | None = Field(default_factory=lambda: None, alias="secretName")

    share_name: str | None = Field(default_factory=lambda: None, alias="shareName")

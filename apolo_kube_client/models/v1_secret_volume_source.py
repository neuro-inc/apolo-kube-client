from __future__ import annotations

from pydantic import BaseModel, Field

from .v1_key_to_path import V1KeyToPath

__all__ = ("V1SecretVolumeSource",)


class V1SecretVolumeSource(BaseModel):
    default_mode: int | None = Field(None, alias="defaultMode")

    items: list[V1KeyToPath] | None = Field(None, alias="items")

    optional: bool | None = Field(None, alias="optional")

    secret_name: str | None = Field(None, alias="secretName")

from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_key_to_path import V1KeyToPath

__all__ = ("V1ConfigMapVolumeSource",)


class V1ConfigMapVolumeSource(BaseModel):
    default_mode: int | None = Field(default_factory=lambda: None, alias="defaultMode")

    items: list[V1KeyToPath] = Field(default_factory=lambda: [])

    name: str | None = Field(default_factory=lambda: None)

    optional: bool | None = Field(default_factory=lambda: None)

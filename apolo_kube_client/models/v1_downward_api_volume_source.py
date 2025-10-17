from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_downward_api_volume_file import V1DownwardAPIVolumeFile

__all__ = ("V1DownwardAPIVolumeSource",)


class V1DownwardAPIVolumeSource(BaseModel):
    default_mode: int | None = Field(default_factory=lambda: None, alias="defaultMode")

    items: list[V1DownwardAPIVolumeFile] = Field(default_factory=lambda: [])

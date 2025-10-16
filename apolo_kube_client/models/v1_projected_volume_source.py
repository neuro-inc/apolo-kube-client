from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_volume_projection import V1VolumeProjection

__all__ = ("V1ProjectedVolumeSource",)


class V1ProjectedVolumeSource(BaseModel):
    default_mode: int | None = Field(default_factory=lambda: None, alias="defaultMode")

    sources: list[V1VolumeProjection] = Field(
        default_factory=lambda: [], alias="sources"
    )

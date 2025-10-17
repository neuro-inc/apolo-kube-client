from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_volume_projection import V1VolumeProjection

__all__ = ("V1ProjectedVolumeSource",)


class V1ProjectedVolumeSource(BaseModel):
    default_mode: int | None = Field(
        default=None,
        serialization_alias="defaultMode",
        validation_alias=AliasChoices("default_mode", "defaultMode"),
    )

    sources: list[V1VolumeProjection] = Field(default=[])

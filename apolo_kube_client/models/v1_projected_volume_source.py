from pydantic import BaseModel, Field

from .v1_volume_projection import V1VolumeProjection


class V1ProjectedVolumeSource(BaseModel):
    default_mode: int | None = Field(None, alias="defaultMode")

    sources: list[V1VolumeProjection] | None = Field(None, alias="sources")

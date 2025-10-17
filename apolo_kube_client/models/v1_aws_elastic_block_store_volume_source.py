from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1AWSElasticBlockStoreVolumeSource",)


class V1AWSElasticBlockStoreVolumeSource(BaseModel):
    fs_type: str | None = Field(default_factory=lambda: None, alias="fsType")

    partition: int | None = Field(default_factory=lambda: None)

    read_only: bool | None = Field(default_factory=lambda: None, alias="readOnly")

    volume_id: str | None = Field(default_factory=lambda: None, alias="volumeID")

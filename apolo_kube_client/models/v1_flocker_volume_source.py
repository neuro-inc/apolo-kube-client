from __future__ import annotations

from pydantic import BaseModel, Field

__all__ = ("V1FlockerVolumeSource",)


class V1FlockerVolumeSource(BaseModel):
    dataset_name: str | None = Field(None, alias="datasetName")

    dataset_uuid: str | None = Field(None, alias="datasetUUID")

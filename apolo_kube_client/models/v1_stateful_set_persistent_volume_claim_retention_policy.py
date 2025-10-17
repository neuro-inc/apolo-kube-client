from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1StatefulSetPersistentVolumeClaimRetentionPolicy",)


class V1StatefulSetPersistentVolumeClaimRetentionPolicy(BaseModel):
    when_deleted: str | None = Field(default_factory=lambda: None, alias="whenDeleted")

    when_scaled: str | None = Field(default_factory=lambda: None, alias="whenScaled")

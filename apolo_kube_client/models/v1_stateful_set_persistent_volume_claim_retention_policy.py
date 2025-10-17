from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field


__all__ = ("V1StatefulSetPersistentVolumeClaimRetentionPolicy",)


class V1StatefulSetPersistentVolumeClaimRetentionPolicy(BaseModel):
    when_deleted: str | None = Field(
        default=None,
        serialization_alias="whenDeleted",
        validation_alias=AliasChoices("when_deleted", "whenDeleted"),
    )

    when_scaled: str | None = Field(
        default=None,
        serialization_alias="whenScaled",
        validation_alias=AliasChoices("when_scaled", "whenScaled"),
    )

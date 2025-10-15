from pydantic import BaseModel, Field


class V1StatefulSetPersistentVolumeClaimRetentionPolicy(BaseModel):
    when_deleted: str | None = Field(None, alias="whenDeleted")

    when_scaled: str | None = Field(None, alias="whenScaled")

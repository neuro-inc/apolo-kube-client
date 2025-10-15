from pydantic import BaseModel, Field

from .v1_persistent_volume_claim_template import V1PersistentVolumeClaimTemplate


class V1EphemeralVolumeSource(BaseModel):
    volume_claim_template: V1PersistentVolumeClaimTemplate | None = Field(
        None, alias="volumeClaimTemplate"
    )

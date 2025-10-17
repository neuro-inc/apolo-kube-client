from pydantic import AliasChoices, BaseModel, Field
from .v1_persistent_volume_claim_template import V1PersistentVolumeClaimTemplate

__all__ = ("V1EphemeralVolumeSource",)


class V1EphemeralVolumeSource(BaseModel):
    volume_claim_template: V1PersistentVolumeClaimTemplate = Field(
        default_factory=lambda: V1PersistentVolumeClaimTemplate(),
        serialization_alias="volumeClaimTemplate",
        validation_alias=AliasChoices("volume_claim_template", "volumeClaimTemplate"),
    )

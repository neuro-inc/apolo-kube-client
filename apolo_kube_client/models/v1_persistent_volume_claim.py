from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_object_meta import V1ObjectMeta
from .v1_persistent_volume_claim_spec import V1PersistentVolumeClaimSpec
from .v1_persistent_volume_claim_status import V1PersistentVolumeClaimStatus

__all__ = ("V1PersistentVolumeClaim",)


class V1PersistentVolumeClaim(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    kind: str | None = Field(default=None)

    metadata: V1ObjectMeta

    spec: V1PersistentVolumeClaimSpec = Field(
        default_factory=lambda: V1PersistentVolumeClaimSpec()
    )

    status: V1PersistentVolumeClaimStatus = Field(
        default_factory=lambda: V1PersistentVolumeClaimStatus()
    )

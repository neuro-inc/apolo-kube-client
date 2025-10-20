from pydantic import AliasChoices, Field
from .base import ResourceModel
from .v1_object_meta import V1ObjectMeta
from .v1_persistent_volume_claim_spec import V1PersistentVolumeClaimSpec
from .v1_persistent_volume_claim_status import V1PersistentVolumeClaimStatus

__all__ = ("V1PersistentVolumeClaim",)


class V1PersistentVolumeClaim(ResourceModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    kind: str | None = None

    metadata: V1ObjectMeta = Field(default_factory=lambda: V1ObjectMeta())

    spec: V1PersistentVolumeClaimSpec = Field(
        default_factory=lambda: V1PersistentVolumeClaimSpec()
    )

    status: V1PersistentVolumeClaimStatus = Field(
        default_factory=lambda: V1PersistentVolumeClaimStatus()
    )

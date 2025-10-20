from pydantic import Field
from .base import ResourceModel
from .v1_object_meta import V1ObjectMeta
from .v1_persistent_volume_claim_spec import V1PersistentVolumeClaimSpec

__all__ = ("V1PersistentVolumeClaimTemplate",)


class V1PersistentVolumeClaimTemplate(ResourceModel):
    metadata: V1ObjectMeta = Field(default_factory=lambda: V1ObjectMeta())

    spec: V1PersistentVolumeClaimSpec = Field(
        default_factory=lambda: V1PersistentVolumeClaimSpec()
    )

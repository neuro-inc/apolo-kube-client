from pydantic import BaseModel, Field

from .v1_object_meta import V1ObjectMeta
from .v1_persistent_volume_claim_spec import V1PersistentVolumeClaimSpec
from .v1_persistent_volume_claim_status import V1PersistentVolumeClaimStatus


class V1PersistentVolumeClaim(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ObjectMeta | None = Field(None, alias="metadata")

    spec: V1PersistentVolumeClaimSpec | None = Field(None, alias="spec")

    status: V1PersistentVolumeClaimStatus | None = Field(None, alias="status")

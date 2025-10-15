from pydantic import BaseModel, Field

from .v1_object_meta import V1ObjectMeta
from .v1_persistent_volume_claim_spec import V1PersistentVolumeClaimSpec


class V1PersistentVolumeClaimTemplate(BaseModel):
    metadata: V1ObjectMeta | None = Field(None, alias="metadata")

    spec: V1PersistentVolumeClaimSpec | None = Field(None, alias="spec")

from pydantic import BaseModel, Field

from .v1_object_meta import V1ObjectMeta
from .v1beta1_resource_claim_spec import V1beta1ResourceClaimSpec


class V1beta1ResourceClaimTemplateSpec(BaseModel):
    metadata: V1ObjectMeta | None = Field(None, alias="metadata")

    spec: V1beta1ResourceClaimSpec | None = Field(None, alias="spec")

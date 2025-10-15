from pydantic import BaseModel, Field

from .v1_object_meta import V1ObjectMeta
from .v1alpha3_resource_claim_spec import V1alpha3ResourceClaimSpec
from .v1alpha3_resource_claim_status import V1alpha3ResourceClaimStatus


class V1alpha3ResourceClaim(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ObjectMeta | None = Field(None, alias="metadata")

    spec: V1alpha3ResourceClaimSpec | None = Field(None, alias="spec")

    status: V1alpha3ResourceClaimStatus | None = Field(None, alias="status")

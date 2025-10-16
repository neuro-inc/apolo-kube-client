from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_object_meta import V1ObjectMeta
from .v1_resource_claim_spec import V1ResourceClaimSpec
from .v1_resource_claim_status import V1ResourceClaimStatus

__all__ = ("ResourceV1ResourceClaim",)


class ResourceV1ResourceClaim(BaseModel):
    api_version: str | None = Field(default_factory=lambda: None, alias="apiVersion")

    kind: str | None = Field(default_factory=lambda: None, alias="kind")

    metadata: V1ObjectMeta = Field(
        default_factory=lambda: V1ObjectMeta(), alias="metadata"
    )

    spec: V1ResourceClaimSpec = Field(
        default_factory=lambda: V1ResourceClaimSpec(), alias="spec"
    )

    status: V1ResourceClaimStatus = Field(
        default_factory=lambda: V1ResourceClaimStatus(), alias="status"
    )

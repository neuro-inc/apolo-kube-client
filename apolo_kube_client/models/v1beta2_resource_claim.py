from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_object_meta import V1ObjectMeta
from .v1beta2_resource_claim_spec import V1beta2ResourceClaimSpec
from .v1beta2_resource_claim_status import V1beta2ResourceClaimStatus

__all__ = ("V1beta2ResourceClaim",)


class V1beta2ResourceClaim(BaseModel):
    api_version: str | None = Field(default_factory=lambda: None, alias="apiVersion")

    kind: str | None = Field(default_factory=lambda: None, alias="kind")

    metadata: V1ObjectMeta = Field(
        default_factory=lambda: V1ObjectMeta(), alias="metadata"
    )

    spec: V1beta2ResourceClaimSpec = Field(
        default_factory=lambda: V1beta2ResourceClaimSpec(), alias="spec"
    )

    status: V1beta2ResourceClaimStatus = Field(
        default_factory=lambda: V1beta2ResourceClaimStatus(), alias="status"
    )

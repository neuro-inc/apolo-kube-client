from __future__ import annotations

from pydantic import BaseModel, Field

from .v1_object_meta import V1ObjectMeta
from .v1beta1_resource_claim_spec import V1beta1ResourceClaimSpec
from .v1beta1_resource_claim_status import V1beta1ResourceClaimStatus

__all__ = ("V1beta1ResourceClaim",)


class V1beta1ResourceClaim(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ObjectMeta | None = Field(None, alias="metadata")

    spec: V1beta1ResourceClaimSpec | None = Field(None, alias="spec")

    status: V1beta1ResourceClaimStatus | None = Field(None, alias="status")

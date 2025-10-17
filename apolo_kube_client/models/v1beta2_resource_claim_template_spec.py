from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_object_meta import V1ObjectMeta
from .v1beta2_resource_claim_spec import V1beta2ResourceClaimSpec

__all__ = ("V1beta2ResourceClaimTemplateSpec",)


class V1beta2ResourceClaimTemplateSpec(BaseModel):
    metadata: V1ObjectMeta

    spec: V1beta2ResourceClaimSpec = Field(
        default_factory=lambda: V1beta2ResourceClaimSpec()
    )

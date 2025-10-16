from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_object_meta import V1ObjectMeta
from .v1_resource_claim_spec import V1ResourceClaimSpec

__all__ = ("V1ResourceClaimTemplateSpec",)


class V1ResourceClaimTemplateSpec(BaseModel):
    metadata: V1ObjectMeta = Field(
        default_factory=lambda: V1ObjectMeta(), alias="metadata"
    )

    spec: V1ResourceClaimSpec = Field(
        default_factory=lambda: V1ResourceClaimSpec(), alias="spec"
    )

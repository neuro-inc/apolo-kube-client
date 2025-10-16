from __future__ import annotations

from pydantic import BaseModel, Field

from .v1_object_meta import V1ObjectMeta
from .v1alpha3_resource_claim_spec import V1alpha3ResourceClaimSpec

__all__ = ("V1alpha3ResourceClaimTemplateSpec",)


class V1alpha3ResourceClaimTemplateSpec(BaseModel):
    metadata: V1ObjectMeta | None = Field(None, alias="metadata")

    spec: V1alpha3ResourceClaimSpec | None = Field(None, alias="spec")

from pydantic import Field
from .base import ResourceModel
from .v1_object_meta import V1ObjectMeta
from .v1beta2_resource_claim_spec import V1beta2ResourceClaimSpec

__all__ = ("V1beta2ResourceClaimTemplateSpec",)


class V1beta2ResourceClaimTemplateSpec(ResourceModel):
    metadata: V1ObjectMeta = Field(default_factory=lambda: V1ObjectMeta())

    spec: V1beta2ResourceClaimSpec = Field(
        default_factory=lambda: V1beta2ResourceClaimSpec()
    )

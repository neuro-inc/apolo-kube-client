from pydantic import Field
from .base import ResourceModel
from .v1_object_meta import V1ObjectMeta
from .v1_resource_claim_spec import V1ResourceClaimSpec

__all__ = ("V1ResourceClaimTemplateSpec",)


class V1ResourceClaimTemplateSpec(ResourceModel):
    metadata: V1ObjectMeta = Field(default_factory=lambda: V1ObjectMeta())

    spec: V1ResourceClaimSpec = Field(default_factory=lambda: V1ResourceClaimSpec())

from pydantic import BaseModel, Field
from .v1_object_meta import V1ObjectMeta
from .v1beta1_resource_claim_spec import V1beta1ResourceClaimSpec

__all__ = ("V1beta1ResourceClaimTemplateSpec",)


class V1beta1ResourceClaimTemplateSpec(BaseModel):
    metadata: V1ObjectMeta = Field(default_factory=lambda: V1ObjectMeta())

    spec: V1beta1ResourceClaimSpec = Field(
        default_factory=lambda: V1beta1ResourceClaimSpec()
    )

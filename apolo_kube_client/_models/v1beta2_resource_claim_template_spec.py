from pydantic import Field
from .base import ResourceModel
from .utils import _default_if_none
from .v1_object_meta import V1ObjectMeta
from .v1beta2_resource_claim_spec import V1beta2ResourceClaimSpec
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1beta2ResourceClaimTemplateSpec",)


class V1beta2ResourceClaimTemplateSpec(ResourceModel):
    metadata: Annotated[
        V1ObjectMeta, BeforeValidator(_default_if_none(V1ObjectMeta))
    ] = Field(default_factory=lambda: V1ObjectMeta())

    spec: Annotated[
        V1beta2ResourceClaimSpec,
        BeforeValidator(_default_if_none(V1beta2ResourceClaimSpec)),
    ] = Field(default_factory=lambda: V1beta2ResourceClaimSpec())

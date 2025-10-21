from pydantic import Field
from .base import ResourceModel
from .utils import _default_if_none
from .v1_object_meta import V1ObjectMeta
from .v1_resource_claim_spec import V1ResourceClaimSpec
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1ResourceClaimTemplateSpec",)


class V1ResourceClaimTemplateSpec(ResourceModel):
    metadata: Annotated[
        V1ObjectMeta, BeforeValidator(_default_if_none(V1ObjectMeta))
    ] = Field(default_factory=lambda: V1ObjectMeta())

    spec: Annotated[
        V1ResourceClaimSpec, BeforeValidator(_default_if_none(V1ResourceClaimSpec))
    ] = Field(default_factory=lambda: V1ResourceClaimSpec())

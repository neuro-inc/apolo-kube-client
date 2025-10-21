from pydantic import AliasChoices, BaseModel, Field
from .base import _default_if_none
from .v1_ingress_load_balancer_status import V1IngressLoadBalancerStatus
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1IngressStatus",)


class V1IngressStatus(BaseModel):
    load_balancer: Annotated[
        V1IngressLoadBalancerStatus,
        BeforeValidator(_default_if_none(V1IngressLoadBalancerStatus)),
    ] = Field(
        default_factory=lambda: V1IngressLoadBalancerStatus(),
        serialization_alias="loadBalancer",
        validation_alias=AliasChoices("load_balancer", "loadBalancer"),
    )

from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_ingress_load_balancer_status import V1IngressLoadBalancerStatus

__all__ = ("V1IngressStatus",)


class V1IngressStatus(BaseModel):
    load_balancer: V1IngressLoadBalancerStatus = Field(
        default_factory=lambda: V1IngressLoadBalancerStatus(), alias="loadBalancer"
    )

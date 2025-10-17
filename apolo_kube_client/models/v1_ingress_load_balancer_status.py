from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_ingress_load_balancer_ingress import V1IngressLoadBalancerIngress

__all__ = ("V1IngressLoadBalancerStatus",)


class V1IngressLoadBalancerStatus(BaseModel):
    ingress: list[V1IngressLoadBalancerIngress] = Field(default=[])

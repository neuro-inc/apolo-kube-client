from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_load_balancer_ingress import V1LoadBalancerIngress

__all__ = ("V1LoadBalancerStatus",)


class V1LoadBalancerStatus(BaseModel):
    ingress: list[V1LoadBalancerIngress] = Field(default_factory=lambda: [])

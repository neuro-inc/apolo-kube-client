from pydantic import BaseModel
from .v1_load_balancer_ingress import V1LoadBalancerIngress

__all__ = ("V1LoadBalancerStatus",)


class V1LoadBalancerStatus(BaseModel):
    ingress: list[V1LoadBalancerIngress] = []

from pydantic import BaseModel
from .v1_ingress_load_balancer_ingress import V1IngressLoadBalancerIngress

__all__ = ("V1IngressLoadBalancerStatus",)


class V1IngressLoadBalancerStatus(BaseModel):
    ingress: list[V1IngressLoadBalancerIngress] = []

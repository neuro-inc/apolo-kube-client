from pydantic import BaseModel, Field

from .v1_ingress_load_balancer_ingress import V1IngressLoadBalancerIngress


class V1IngressLoadBalancerStatus(BaseModel):
    ingress: list[V1IngressLoadBalancerIngress] | None = Field(None, alias="ingress")

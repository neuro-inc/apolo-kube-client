from pydantic import BaseModel, Field

from .v1_load_balancer_ingress import V1LoadBalancerIngress


class V1LoadBalancerStatus(BaseModel):
    ingress: list[V1LoadBalancerIngress] | None = Field(None, alias="ingress")

from pydantic import BaseModel, Field

from .v1_ingress_load_balancer_status import V1IngressLoadBalancerStatus


class V1IngressStatus(BaseModel):
    load_balancer: V1IngressLoadBalancerStatus | None = Field(
        None, alias="loadBalancer"
    )

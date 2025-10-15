from pydantic import BaseModel, Field

from .v1_condition import V1Condition
from .v1_load_balancer_status import V1LoadBalancerStatus


class V1ServiceStatus(BaseModel):
    conditions: list[V1Condition] | None = Field(None, alias="conditions")

    load_balancer: V1LoadBalancerStatus | None = Field(None, alias="loadBalancer")

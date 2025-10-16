from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_condition import V1Condition
from .v1_load_balancer_status import V1LoadBalancerStatus

__all__ = ("V1ServiceStatus",)


class V1ServiceStatus(BaseModel):
    conditions: list[V1Condition] = Field(
        default_factory=lambda: [], alias="conditions"
    )

    load_balancer: V1LoadBalancerStatus = Field(
        default_factory=lambda: V1LoadBalancerStatus(), alias="loadBalancer"
    )

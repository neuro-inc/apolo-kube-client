from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_condition import V1Condition
from .v1_load_balancer_status import V1LoadBalancerStatus

__all__ = ("V1ServiceStatus",)


class V1ServiceStatus(BaseModel):
    conditions: list[V1Condition] = Field(default=[])

    load_balancer: V1LoadBalancerStatus = Field(
        default_factory=lambda: V1LoadBalancerStatus(),
        serialization_alias="loadBalancer",
        validation_alias=AliasChoices("load_balancer", "loadBalancer"),
    )

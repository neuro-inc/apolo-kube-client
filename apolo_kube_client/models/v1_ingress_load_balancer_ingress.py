from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_ingress_port_status import V1IngressPortStatus

__all__ = ("V1IngressLoadBalancerIngress",)


class V1IngressLoadBalancerIngress(BaseModel):
    hostname: str | None = Field(default_factory=lambda: None)

    ip: str | None = Field(default_factory=lambda: None)

    ports: list[V1IngressPortStatus] = Field(default_factory=lambda: [])

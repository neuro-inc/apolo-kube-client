from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_port_status import V1PortStatus

__all__ = ("V1LoadBalancerIngress",)


class V1LoadBalancerIngress(BaseModel):
    hostname: str | None = Field(default_factory=lambda: None)

    ip: str | None = Field(default_factory=lambda: None)

    ip_mode: str | None = Field(default_factory=lambda: None, alias="ipMode")

    ports: list[V1PortStatus] = Field(default_factory=lambda: [])

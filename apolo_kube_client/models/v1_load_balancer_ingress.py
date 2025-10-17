from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_port_status import V1PortStatus

__all__ = ("V1LoadBalancerIngress",)


class V1LoadBalancerIngress(BaseModel):
    hostname: str | None = Field(default=None)

    ip: str | None = Field(default=None)

    ip_mode: str | None = Field(
        default=None,
        serialization_alias="ipMode",
        validation_alias=AliasChoices("ip_mode", "ipMode"),
    )

    ports: list[V1PortStatus] = Field(default=[])

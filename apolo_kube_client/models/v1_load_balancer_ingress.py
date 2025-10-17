from pydantic import AliasChoices, BaseModel, Field
from .v1_port_status import V1PortStatus

__all__ = ("V1LoadBalancerIngress",)


class V1LoadBalancerIngress(BaseModel):
    hostname: str | None = None

    ip: str | None = None

    ip_mode: str | None = Field(
        default=None,
        serialization_alias="ipMode",
        validation_alias=AliasChoices("ip_mode", "ipMode"),
    )

    ports: list[V1PortStatus] = []

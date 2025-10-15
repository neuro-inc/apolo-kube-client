from pydantic import BaseModel, Field

from .v1_ingress_port_status import V1IngressPortStatus


class V1IngressLoadBalancerIngress(BaseModel):
    hostname: str | None = Field(None, alias="hostname")

    ip: str | None = Field(None, alias="ip")

    ports: list[V1IngressPortStatus] | None = Field(None, alias="ports")

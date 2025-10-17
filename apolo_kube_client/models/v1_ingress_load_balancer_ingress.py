from pydantic import BaseModel
from .v1_ingress_port_status import V1IngressPortStatus

__all__ = ("V1IngressLoadBalancerIngress",)


class V1IngressLoadBalancerIngress(BaseModel):
    hostname: str | None = None

    ip: str | None = None

    ports: list[V1IngressPortStatus] = []

from pydantic import BaseModel
from .utils import _collection_if_none
from .v1_ingress_port_status import V1IngressPortStatus
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1IngressLoadBalancerIngress",)


class V1IngressLoadBalancerIngress(BaseModel):
    hostname: str | None = None

    ip: str | None = None

    ports: Annotated[
        list[V1IngressPortStatus], BeforeValidator(_collection_if_none("[]"))
    ] = []

from pydantic import BaseModel, Field
from .utils import _collection_if_none
from .utils import _exclude_if
from .v1_ingress_port_status import V1IngressPortStatus
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1IngressLoadBalancerIngress",)


class V1IngressLoadBalancerIngress(BaseModel):
    hostname: str | None = Field(default=None, exclude_if=_exclude_if)

    ip: str | None = Field(default=None, exclude_if=_exclude_if)

    ports: Annotated[
        list[V1IngressPortStatus], BeforeValidator(_collection_if_none("[]"))
    ] = Field(default=[], exclude_if=_exclude_if)

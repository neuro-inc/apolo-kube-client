from pydantic import BaseModel, Field
from .utils import _collection_if_none
from .utils import _exclude_if
from .v1_ingress_load_balancer_ingress import V1IngressLoadBalancerIngress
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1IngressLoadBalancerStatus",)


class V1IngressLoadBalancerStatus(BaseModel):
    ingress: Annotated[
        list[V1IngressLoadBalancerIngress], BeforeValidator(_collection_if_none("[]"))
    ] = Field(default=[], exclude_if=_exclude_if)

from pydantic import BaseModel, Field
from .utils import _collection_if_none
from .utils import _exclude_if
from .v1_load_balancer_ingress import V1LoadBalancerIngress
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1LoadBalancerStatus",)


class V1LoadBalancerStatus(BaseModel):
    ingress: Annotated[
        list[V1LoadBalancerIngress], BeforeValidator(_collection_if_none("[]"))
    ] = Field(default=[], exclude_if=_exclude_if)

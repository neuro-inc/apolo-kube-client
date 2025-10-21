from pydantic import BaseModel
from .utils import _collection_if_none
from .v1_load_balancer_ingress import V1LoadBalancerIngress
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1LoadBalancerStatus",)


class V1LoadBalancerStatus(BaseModel):
    ingress: Annotated[
        list[V1LoadBalancerIngress], BeforeValidator(_collection_if_none("[]"))
    ] = []

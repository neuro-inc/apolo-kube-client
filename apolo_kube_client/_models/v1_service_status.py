from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .utils import _default_if_none
from .v1_condition import V1Condition
from .v1_load_balancer_status import V1LoadBalancerStatus
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1ServiceStatus",)


class V1ServiceStatus(BaseModel):
    conditions: Annotated[
        list[V1Condition], BeforeValidator(_collection_if_none("[]"))
    ] = []

    load_balancer: Annotated[
        V1LoadBalancerStatus, BeforeValidator(_default_if_none(V1LoadBalancerStatus))
    ] = Field(
        default_factory=lambda: V1LoadBalancerStatus(),
        serialization_alias="loadBalancer",
        validation_alias=AliasChoices("load_balancer", "loadBalancer"),
    )

from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _collection_if_none
from .utils import _default_if_none
from .v1_condition import V1Condition
from .v1_load_balancer_status import V1LoadBalancerStatus
from pydantic import BeforeValidator

__all__ = ("V1ServiceStatus",)


class V1ServiceStatus(BaseModel):
    """ServiceStatus represents the current status of a service."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.ServiceStatus"

    conditions: Annotated[
        list[V1Condition],
        Field(description="""Current service state""", exclude_if=lambda v: v == []),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    load_balancer: Annotated[
        V1LoadBalancerStatus,
        Field(
            alias="loadBalancer",
            description="""LoadBalancer contains the current status of the load-balancer, if one is present.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1LoadBalancerStatus)),
    ] = V1LoadBalancerStatus()

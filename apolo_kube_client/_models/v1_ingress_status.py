from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _default_if_none
from .v1_ingress_load_balancer_status import V1IngressLoadBalancerStatus
from pydantic import BeforeValidator

__all__ = ("V1IngressStatus",)


class V1IngressStatus(BaseModel):
    """IngressStatus describe the current state of the Ingress."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.networking.v1.IngressStatus"

    load_balancer: Annotated[
        V1IngressLoadBalancerStatus,
        Field(
            alias="loadBalancer",
            description="""loadBalancer contains the current status of the load-balancer.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1IngressLoadBalancerStatus)),
    ] = V1IngressLoadBalancerStatus()

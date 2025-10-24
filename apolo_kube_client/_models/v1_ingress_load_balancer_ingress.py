from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _collection_if_none
from .v1_ingress_port_status import V1IngressPortStatus
from pydantic import BeforeValidator

__all__ = ("V1IngressLoadBalancerIngress",)


class V1IngressLoadBalancerIngress(BaseModel):
    """IngressLoadBalancerIngress represents the status of a load-balancer ingress point."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.networking.v1.IngressLoadBalancerIngress"
    )

    hostname: Annotated[
        str | None,
        Field(
            description="""hostname is set for load-balancer ingress points that are DNS based.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    ip: Annotated[
        str | None,
        Field(
            description="""ip is set for load-balancer ingress points that are IP based.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    ports: Annotated[
        list[V1IngressPortStatus],
        Field(
            description="""ports provides information about the ports exposed by this LoadBalancer.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

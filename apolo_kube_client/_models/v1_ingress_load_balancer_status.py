from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _collection_if_none
from .v1_ingress_load_balancer_ingress import V1IngressLoadBalancerIngress
from pydantic import BeforeValidator

__all__ = ("V1IngressLoadBalancerStatus",)


class V1IngressLoadBalancerStatus(BaseModel):
    """IngressLoadBalancerStatus represents the status of a load-balancer."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.networking.v1.IngressLoadBalancerStatus"
    )

    ingress: Annotated[
        list[V1IngressLoadBalancerIngress],
        Field(
            description="""ingress is a list containing ingress points for the load-balancer.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

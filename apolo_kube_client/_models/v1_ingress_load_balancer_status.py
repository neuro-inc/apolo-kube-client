from typing import Annotated, ClassVar, Final

from pydantic import BeforeValidator, Field

from .base_model import BaseConfiguredModel
from .utils import _collection_if_none
from .v1_ingress_load_balancer_ingress import V1IngressLoadBalancerIngress


__all__ = ("V1IngressLoadBalancerStatus",)


class V1IngressLoadBalancerStatus(BaseConfiguredModel):
    """IngressLoadBalancerStatus represents the status of a load-balancer."""

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

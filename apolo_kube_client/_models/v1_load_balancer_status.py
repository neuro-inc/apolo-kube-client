from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _collection_if_none
from .v1_load_balancer_ingress import V1LoadBalancerIngress
from pydantic import BeforeValidator

__all__ = ("V1LoadBalancerStatus",)


class V1LoadBalancerStatus(BaseModel):
    """LoadBalancerStatus represents the status of a load-balancer."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.LoadBalancerStatus"

    ingress: Annotated[
        list[V1LoadBalancerIngress],
        Field(
            description="""Ingress is a list containing ingress points for the load-balancer. Traffic intended for the service should be sent to these ingress points.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

from typing import Annotated, ClassVar, Final

from pydantic import BeforeValidator, Field

from .base_model import BaseConfiguredModel
from .core_v1_endpoint_port import CoreV1EndpointPort
from .utils import _collection_if_none
from .v1_endpoint_address import V1EndpointAddress


__all__ = ("V1EndpointSubset",)


class V1EndpointSubset(BaseConfiguredModel):
    """EndpointSubset is a group of addresses with a common set of ports. The expanded set of endpoints is the Cartesian product of Addresses x Ports. For example, given:

            {
              Addresses: [{"ip": "10.10.1.1"}, {"ip": "10.10.2.2"}],
              Ports:     [{"name": "a", "port": 8675}, {"name": "b", "port": 309}]
            }

    The resulting set of endpoints can be viewed as:

            a: [ 10.10.1.1:8675, 10.10.2.2:8675 ],
            b: [ 10.10.1.1:309, 10.10.2.2:309 ]

    Deprecated: This API is deprecated in v1.33+."""

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.EndpointSubset"

    addresses: Annotated[
        list[V1EndpointAddress],
        Field(
            description="""IP addresses which offer the related ports that are marked as ready. These endpoints should be considered safe for load balancers and clients to utilize.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    not_ready_addresses: Annotated[
        list[V1EndpointAddress],
        Field(
            alias="notReadyAddresses",
            description="""IP addresses which offer the related ports but are not currently marked as ready because they have not yet finished starting, have recently failed a readiness check, or have recently failed a liveness check.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    ports: Annotated[
        list[CoreV1EndpointPort],
        Field(
            description="""Port numbers available on the related IP addresses.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

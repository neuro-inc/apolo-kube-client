from pydantic import AliasChoices, Field
from .base import ResourceModel
from .discovery_v1_endpoint_port import DiscoveryV1EndpointPort
from .v1_endpoint import V1Endpoint
from .v1_object_meta import V1ObjectMeta

__all__ = ("V1EndpointSlice",)


class V1EndpointSlice(ResourceModel):
    address_type: str | None = Field(
        default=None,
        serialization_alias="addressType",
        validation_alias=AliasChoices("address_type", "addressType"),
    )

    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    endpoints: list[V1Endpoint] = []

    kind: str | None = None

    metadata: V1ObjectMeta = Field(default_factory=lambda: V1ObjectMeta())

    ports: list[DiscoveryV1EndpointPort] = []

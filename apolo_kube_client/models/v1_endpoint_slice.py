from __future__ import annotations
from pydantic import BaseModel, Field
from .discovery_v1_endpoint_port import DiscoveryV1EndpointPort
from .v1_endpoint import V1Endpoint
from .v1_object_meta import V1ObjectMeta

__all__ = ("V1EndpointSlice",)


class V1EndpointSlice(BaseModel):
    address_type: str | None = Field(default_factory=lambda: None, alias="addressType")

    api_version: str | None = Field(default_factory=lambda: None, alias="apiVersion")

    endpoints: list[V1Endpoint] = Field(default_factory=lambda: [])

    kind: str | None = Field(default_factory=lambda: None)

    metadata: V1ObjectMeta = Field(default_factory=lambda: V1ObjectMeta())

    ports: list[DiscoveryV1EndpointPort] = Field(default_factory=lambda: [])

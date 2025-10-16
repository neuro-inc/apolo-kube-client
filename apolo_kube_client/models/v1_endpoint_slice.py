from __future__ import annotations

from pydantic import BaseModel, Field

from .discovery_v1_endpoint_port import DiscoveryV1EndpointPort
from .v1_endpoint import V1Endpoint
from .v1_object_meta import V1ObjectMeta

__all__ = ("V1EndpointSlice",)


class V1EndpointSlice(BaseModel):
    address_type: str | None = Field(None, alias="addressType")

    api_version: str | None = Field(None, alias="apiVersion")

    endpoints: list[V1Endpoint] | None = Field(None, alias="endpoints")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ObjectMeta | None = Field(None, alias="metadata")

    ports: list[DiscoveryV1EndpointPort] | None = Field(None, alias="ports")

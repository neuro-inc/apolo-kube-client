from pydantic import BaseModel, Field

from .v1_endpoint_conditions import V1EndpointConditions
from .v1_endpoint_hints import V1EndpointHints
from .v1_object_reference import V1ObjectReference


class V1Endpoint(BaseModel):
    addresses: list[str] | None = Field(None, alias="addresses")

    conditions: V1EndpointConditions | None = Field(None, alias="conditions")

    deprecated_topology: dict(str, str) | None = Field(None, alias="deprecatedTopology")

    hints: V1EndpointHints | None = Field(None, alias="hints")

    hostname: str | None = Field(None, alias="hostname")

    node_name: str | None = Field(None, alias="nodeName")

    target_ref: V1ObjectReference | None = Field(None, alias="targetRef")

    zone: str | None = Field(None, alias="zone")

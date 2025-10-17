from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_endpoint_conditions import V1EndpointConditions
from .v1_endpoint_hints import V1EndpointHints
from .v1_object_reference import V1ObjectReference

__all__ = ("V1Endpoint",)


class V1Endpoint(BaseModel):
    addresses: list[str] = Field(default_factory=lambda: [])

    conditions: V1EndpointConditions = Field(
        default_factory=lambda: V1EndpointConditions()
    )

    deprecated_topology: dict[str, str] = Field(
        default_factory=lambda: {}, alias="deprecatedTopology"
    )

    hints: V1EndpointHints = Field(default_factory=lambda: V1EndpointHints())

    hostname: str | None = Field(default_factory=lambda: None)

    node_name: str | None = Field(default_factory=lambda: None, alias="nodeName")

    target_ref: V1ObjectReference = Field(
        default_factory=lambda: V1ObjectReference(), alias="targetRef"
    )

    zone: str | None = Field(default_factory=lambda: None)

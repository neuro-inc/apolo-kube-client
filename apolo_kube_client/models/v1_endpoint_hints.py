from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_for_node import V1ForNode
from .v1_for_zone import V1ForZone

__all__ = ("V1EndpointHints",)


class V1EndpointHints(BaseModel):
    for_nodes: list[V1ForNode] = Field(default_factory=lambda: [], alias="forNodes")

    for_zones: list[V1ForZone] = Field(default_factory=lambda: [], alias="forZones")

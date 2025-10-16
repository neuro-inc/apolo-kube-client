from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_volume_node_resources import V1VolumeNodeResources

__all__ = ("V1CSINodeDriver",)


class V1CSINodeDriver(BaseModel):
    allocatable: V1VolumeNodeResources = Field(
        default_factory=lambda: V1VolumeNodeResources(), alias="allocatable"
    )

    name: str | None = Field(default_factory=lambda: None, alias="name")

    node_id: str | None = Field(default_factory=lambda: None, alias="nodeID")

    topology_keys: list[str] = Field(default_factory=lambda: [], alias="topologyKeys")

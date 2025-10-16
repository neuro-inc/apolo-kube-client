from __future__ import annotations

from pydantic import BaseModel, Field

from .v1_volume_node_resources import V1VolumeNodeResources

__all__ = ("V1CSINodeDriver",)


class V1CSINodeDriver(BaseModel):
    allocatable: V1VolumeNodeResources | None = Field(None, alias="allocatable")

    name: str | None = Field(None, alias="name")

    node_id: str | None = Field(None, alias="nodeID")

    topology_keys: list[str] | None = Field(None, alias="topologyKeys")

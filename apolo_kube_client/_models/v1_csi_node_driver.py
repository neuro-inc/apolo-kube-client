from pydantic import AliasChoices, BaseModel, Field
from .v1_volume_node_resources import V1VolumeNodeResources

__all__ = ("V1CSINodeDriver",)


class V1CSINodeDriver(BaseModel):
    allocatable: V1VolumeNodeResources = Field(
        default_factory=lambda: V1VolumeNodeResources()
    )

    name: str | None = None

    node_id: str | None = Field(
        default=None,
        serialization_alias="nodeID",
        validation_alias=AliasChoices("node_id", "nodeID"),
    )

    topology_keys: list[str] = Field(
        default=[],
        serialization_alias="topologyKeys",
        validation_alias=AliasChoices("topology_keys", "topologyKeys"),
    )

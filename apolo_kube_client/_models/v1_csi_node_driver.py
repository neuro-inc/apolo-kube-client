from pydantic import AliasChoices, BaseModel, Field
from .base import _default_if_none
from .v1_volume_node_resources import V1VolumeNodeResources
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1CSINodeDriver",)


class V1CSINodeDriver(BaseModel):
    allocatable: Annotated[
        V1VolumeNodeResources, BeforeValidator(_default_if_none(V1VolumeNodeResources))
    ] = Field(default_factory=lambda: V1VolumeNodeResources())

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

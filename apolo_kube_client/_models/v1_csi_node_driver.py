from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .utils import _default_if_none
from .utils import _exclude_if
from .v1_volume_node_resources import V1VolumeNodeResources
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1CSINodeDriver",)


class V1CSINodeDriver(BaseModel):
    allocatable: Annotated[
        V1VolumeNodeResources, BeforeValidator(_default_if_none(V1VolumeNodeResources))
    ] = Field(default_factory=lambda: V1VolumeNodeResources(), exclude_if=_exclude_if)

    name: str | None = Field(default=None, exclude_if=_exclude_if)

    node_id: str | None = Field(
        default=None,
        serialization_alias="nodeID",
        validation_alias=AliasChoices("node_id", "nodeID"),
        exclude_if=_exclude_if,
    )

    topology_keys: Annotated[list[str], BeforeValidator(_collection_if_none("[]"))] = (
        Field(
            default=[],
            serialization_alias="topologyKeys",
            validation_alias=AliasChoices("topology_keys", "topologyKeys"),
            exclude_if=_exclude_if,
        )
    )

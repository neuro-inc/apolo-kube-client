from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .utils import _default_if_none
from .utils import _exclude_if
from .v1_node_selector import V1NodeSelector
from .v1beta1_counter_set import V1beta1CounterSet
from .v1beta1_device import V1beta1Device
from .v1beta1_resource_pool import V1beta1ResourcePool
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1beta1ResourceSliceSpec",)


class V1beta1ResourceSliceSpec(BaseModel):
    all_nodes: bool | None = Field(
        default=None,
        serialization_alias="allNodes",
        validation_alias=AliasChoices("all_nodes", "allNodes"),
        exclude_if=_exclude_if,
    )

    devices: Annotated[
        list[V1beta1Device], BeforeValidator(_collection_if_none("[]"))
    ] = Field(default=[], exclude_if=_exclude_if)

    driver: str | None = Field(default=None, exclude_if=_exclude_if)

    node_name: str | None = Field(
        default=None,
        serialization_alias="nodeName",
        validation_alias=AliasChoices("node_name", "nodeName"),
        exclude_if=_exclude_if,
    )

    node_selector: Annotated[
        V1NodeSelector, BeforeValidator(_default_if_none(V1NodeSelector))
    ] = Field(
        default_factory=lambda: V1NodeSelector(),
        serialization_alias="nodeSelector",
        validation_alias=AliasChoices("node_selector", "nodeSelector"),
        exclude_if=_exclude_if,
    )

    per_device_node_selection: bool | None = Field(
        default=None,
        serialization_alias="perDeviceNodeSelection",
        validation_alias=AliasChoices(
            "per_device_node_selection", "perDeviceNodeSelection"
        ),
        exclude_if=_exclude_if,
    )

    pool: Annotated[
        V1beta1ResourcePool, BeforeValidator(_default_if_none(V1beta1ResourcePool))
    ] = Field(default_factory=lambda: V1beta1ResourcePool(), exclude_if=_exclude_if)

    shared_counters: Annotated[
        list[V1beta1CounterSet], BeforeValidator(_collection_if_none("[]"))
    ] = Field(
        default=[],
        serialization_alias="sharedCounters",
        validation_alias=AliasChoices("shared_counters", "sharedCounters"),
        exclude_if=_exclude_if,
    )

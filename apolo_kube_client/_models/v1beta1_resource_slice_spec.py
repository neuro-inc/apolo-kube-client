from pydantic import AliasChoices, BaseModel, Field
from .base import _default_if_none
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
    )

    devices: list[V1beta1Device] = []

    driver: str | None = None

    node_name: str | None = Field(
        default=None,
        serialization_alias="nodeName",
        validation_alias=AliasChoices("node_name", "nodeName"),
    )

    node_selector: Annotated[
        V1NodeSelector, BeforeValidator(_default_if_none(V1NodeSelector))
    ] = Field(
        default_factory=lambda: V1NodeSelector(),
        serialization_alias="nodeSelector",
        validation_alias=AliasChoices("node_selector", "nodeSelector"),
    )

    per_device_node_selection: bool | None = Field(
        default=None,
        serialization_alias="perDeviceNodeSelection",
        validation_alias=AliasChoices(
            "per_device_node_selection", "perDeviceNodeSelection"
        ),
    )

    pool: Annotated[
        V1beta1ResourcePool, BeforeValidator(_default_if_none(V1beta1ResourcePool))
    ] = Field(default_factory=lambda: V1beta1ResourcePool())

    shared_counters: list[V1beta1CounterSet] = Field(
        default=[],
        serialization_alias="sharedCounters",
        validation_alias=AliasChoices("shared_counters", "sharedCounters"),
    )

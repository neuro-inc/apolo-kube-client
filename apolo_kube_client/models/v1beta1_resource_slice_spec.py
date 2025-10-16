from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_node_selector import V1NodeSelector
from .v1beta1_counter_set import V1beta1CounterSet
from .v1beta1_device import V1beta1Device
from .v1beta1_resource_pool import V1beta1ResourcePool

__all__ = ("V1beta1ResourceSliceSpec",)


class V1beta1ResourceSliceSpec(BaseModel):
    all_nodes: bool | None = Field(default_factory=lambda: None, alias="allNodes")

    devices: list[V1beta1Device] = Field(default_factory=lambda: [], alias="devices")

    driver: str | None = Field(default_factory=lambda: None, alias="driver")

    node_name: str | None = Field(default_factory=lambda: None, alias="nodeName")

    node_selector: V1NodeSelector = Field(
        default_factory=lambda: V1NodeSelector(), alias="nodeSelector"
    )

    per_device_node_selection: bool | None = Field(
        default_factory=lambda: None, alias="perDeviceNodeSelection"
    )

    pool: V1beta1ResourcePool = Field(
        default_factory=lambda: V1beta1ResourcePool(), alias="pool"
    )

    shared_counters: list[V1beta1CounterSet] = Field(
        default_factory=lambda: [], alias="sharedCounters"
    )

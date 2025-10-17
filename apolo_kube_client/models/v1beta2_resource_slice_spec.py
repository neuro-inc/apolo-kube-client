from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_node_selector import V1NodeSelector
from .v1beta2_counter_set import V1beta2CounterSet
from .v1beta2_device import V1beta2Device
from .v1beta2_resource_pool import V1beta2ResourcePool

__all__ = ("V1beta2ResourceSliceSpec",)


class V1beta2ResourceSliceSpec(BaseModel):
    all_nodes: bool | None = Field(default_factory=lambda: None, alias="allNodes")

    devices: list[V1beta2Device] = Field(default_factory=lambda: [])

    driver: str | None = Field(default_factory=lambda: None)

    node_name: str | None = Field(default_factory=lambda: None, alias="nodeName")

    node_selector: V1NodeSelector = Field(
        default_factory=lambda: V1NodeSelector(), alias="nodeSelector"
    )

    per_device_node_selection: bool | None = Field(
        default_factory=lambda: None, alias="perDeviceNodeSelection"
    )

    pool: V1beta2ResourcePool = Field(default_factory=lambda: V1beta2ResourcePool())

    shared_counters: list[V1beta2CounterSet] = Field(
        default_factory=lambda: [], alias="sharedCounters"
    )

from pydantic import AliasChoices, BaseModel, Field
from .v1_node_selector import V1NodeSelector
from .v1beta2_counter_set import V1beta2CounterSet
from .v1beta2_device import V1beta2Device
from .v1beta2_resource_pool import V1beta2ResourcePool

__all__ = ("V1beta2ResourceSliceSpec",)


class V1beta2ResourceSliceSpec(BaseModel):
    all_nodes: bool | None = Field(
        default=None,
        serialization_alias="allNodes",
        validation_alias=AliasChoices("all_nodes", "allNodes"),
    )

    devices: list[V1beta2Device] = []

    driver: str | None = None

    node_name: str | None = Field(
        default=None,
        serialization_alias="nodeName",
        validation_alias=AliasChoices("node_name", "nodeName"),
    )

    node_selector: V1NodeSelector = Field(
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

    pool: V1beta2ResourcePool = Field(default_factory=lambda: V1beta2ResourcePool())

    shared_counters: list[V1beta2CounterSet] = Field(
        default=[],
        serialization_alias="sharedCounters",
        validation_alias=AliasChoices("shared_counters", "sharedCounters"),
    )

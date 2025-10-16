from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_node_selector import V1NodeSelector
from .v1beta1_device_attribute import V1beta1DeviceAttribute
from .v1beta1_device_capacity import V1beta1DeviceCapacity
from .v1beta1_device_counter_consumption import V1beta1DeviceCounterConsumption
from .v1beta1_device_taint import V1beta1DeviceTaint

__all__ = ("V1beta1BasicDevice",)


class V1beta1BasicDevice(BaseModel):
    all_nodes: bool | None = Field(default_factory=lambda: None, alias="allNodes")

    allow_multiple_allocations: bool | None = Field(
        default_factory=lambda: None, alias="allowMultipleAllocations"
    )

    attributes: dict[str, V1beta1DeviceAttribute] = Field(
        default_factory=lambda: {}, alias="attributes"
    )

    binding_conditions: list[str] = Field(
        default_factory=lambda: [], alias="bindingConditions"
    )

    binding_failure_conditions: list[str] = Field(
        default_factory=lambda: [], alias="bindingFailureConditions"
    )

    binds_to_node: bool | None = Field(
        default_factory=lambda: None, alias="bindsToNode"
    )

    capacity: dict[str, V1beta1DeviceCapacity] = Field(
        default_factory=lambda: {}, alias="capacity"
    )

    consumes_counters: list[V1beta1DeviceCounterConsumption] = Field(
        default_factory=lambda: [], alias="consumesCounters"
    )

    node_name: str | None = Field(default_factory=lambda: None, alias="nodeName")

    node_selector: V1NodeSelector = Field(
        default_factory=lambda: V1NodeSelector(), alias="nodeSelector"
    )

    taints: list[V1beta1DeviceTaint] = Field(default_factory=lambda: [], alias="taints")

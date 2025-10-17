from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_node_selector import V1NodeSelector
from .v1beta1_device_attribute import V1beta1DeviceAttribute
from .v1beta1_device_capacity import V1beta1DeviceCapacity
from .v1beta1_device_counter_consumption import V1beta1DeviceCounterConsumption
from .v1beta1_device_taint import V1beta1DeviceTaint

__all__ = ("V1beta1BasicDevice",)


class V1beta1BasicDevice(BaseModel):
    all_nodes: bool | None = Field(
        default=None,
        serialization_alias="allNodes",
        validation_alias=AliasChoices("all_nodes", "allNodes"),
    )

    allow_multiple_allocations: bool | None = Field(
        default=None,
        serialization_alias="allowMultipleAllocations",
        validation_alias=AliasChoices(
            "allow_multiple_allocations", "allowMultipleAllocations"
        ),
    )

    attributes: dict[str, V1beta1DeviceAttribute] = Field(default={})

    binding_conditions: list[str] = Field(
        default=[],
        serialization_alias="bindingConditions",
        validation_alias=AliasChoices("binding_conditions", "bindingConditions"),
    )

    binding_failure_conditions: list[str] = Field(
        default=[],
        serialization_alias="bindingFailureConditions",
        validation_alias=AliasChoices(
            "binding_failure_conditions", "bindingFailureConditions"
        ),
    )

    binds_to_node: bool | None = Field(
        default=None,
        serialization_alias="bindsToNode",
        validation_alias=AliasChoices("binds_to_node", "bindsToNode"),
    )

    capacity: dict[str, V1beta1DeviceCapacity] = Field(default={})

    consumes_counters: list[V1beta1DeviceCounterConsumption] = Field(
        default=[],
        serialization_alias="consumesCounters",
        validation_alias=AliasChoices("consumes_counters", "consumesCounters"),
    )

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

    taints: list[V1beta1DeviceTaint] = Field(default=[])

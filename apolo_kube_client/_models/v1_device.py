from pydantic import AliasChoices, BaseModel, Field
from .base import _default_if_none
from .v1_device_attribute import V1DeviceAttribute
from .v1_device_capacity import V1DeviceCapacity
from .v1_device_counter_consumption import V1DeviceCounterConsumption
from .v1_device_taint import V1DeviceTaint
from .v1_node_selector import V1NodeSelector
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1Device",)


class V1Device(BaseModel):
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

    attributes: dict[str, V1DeviceAttribute] = {}

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

    capacity: dict[str, V1DeviceCapacity] = {}

    consumes_counters: list[V1DeviceCounterConsumption] = Field(
        default=[],
        serialization_alias="consumesCounters",
        validation_alias=AliasChoices("consumes_counters", "consumesCounters"),
    )

    name: str | None = None

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

    taints: list[V1DeviceTaint] = []

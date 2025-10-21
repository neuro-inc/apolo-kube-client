from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .utils import _default_if_none
from .v1_node_selector import V1NodeSelector
from .v1beta2_device_attribute import V1beta2DeviceAttribute
from .v1beta2_device_capacity import V1beta2DeviceCapacity
from .v1beta2_device_counter_consumption import V1beta2DeviceCounterConsumption
from .v1beta2_device_taint import V1beta2DeviceTaint
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1beta2Device",)


class V1beta2Device(BaseModel):
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

    attributes: Annotated[
        dict[str, V1beta2DeviceAttribute], BeforeValidator(_collection_if_none("{}"))
    ] = {}

    binding_conditions: Annotated[
        list[str], BeforeValidator(_collection_if_none("[]"))
    ] = Field(
        default=[],
        serialization_alias="bindingConditions",
        validation_alias=AliasChoices("binding_conditions", "bindingConditions"),
    )

    binding_failure_conditions: Annotated[
        list[str], BeforeValidator(_collection_if_none("[]"))
    ] = Field(
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

    capacity: Annotated[
        dict[str, V1beta2DeviceCapacity], BeforeValidator(_collection_if_none("{}"))
    ] = {}

    consumes_counters: Annotated[
        list[V1beta2DeviceCounterConsumption],
        BeforeValidator(_collection_if_none("[]")),
    ] = Field(
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

    taints: Annotated[
        list[V1beta2DeviceTaint], BeforeValidator(_collection_if_none("[]"))
    ] = []

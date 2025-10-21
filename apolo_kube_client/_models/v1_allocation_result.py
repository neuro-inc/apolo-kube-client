from pydantic import AliasChoices, BaseModel, Field
from .utils import _default_if_none
from .v1_device_allocation_result import V1DeviceAllocationResult
from .v1_node_selector import V1NodeSelector
from datetime import datetime
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1AllocationResult",)


class V1AllocationResult(BaseModel):
    allocation_timestamp: datetime | None = Field(
        default=None,
        serialization_alias="allocationTimestamp",
        validation_alias=AliasChoices("allocation_timestamp", "allocationTimestamp"),
    )

    devices: Annotated[
        V1DeviceAllocationResult,
        BeforeValidator(_default_if_none(V1DeviceAllocationResult)),
    ] = Field(default_factory=lambda: V1DeviceAllocationResult())

    node_selector: Annotated[
        V1NodeSelector, BeforeValidator(_default_if_none(V1NodeSelector))
    ] = Field(
        default_factory=lambda: V1NodeSelector(),
        serialization_alias="nodeSelector",
        validation_alias=AliasChoices("node_selector", "nodeSelector"),
    )

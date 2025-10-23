from pydantic import AliasChoices, BaseModel, Field
from .utils import _default_if_none
from .utils import _exclude_if
from .v1_node_selector import V1NodeSelector
from .v1beta1_device_allocation_result import V1beta1DeviceAllocationResult
from datetime import datetime
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1beta1AllocationResult",)


class V1beta1AllocationResult(BaseModel):
    allocation_timestamp: datetime | None = Field(
        default=None,
        serialization_alias="allocationTimestamp",
        validation_alias=AliasChoices("allocation_timestamp", "allocationTimestamp"),
        exclude_if=_exclude_if,
    )

    devices: Annotated[
        V1beta1DeviceAllocationResult,
        BeforeValidator(_default_if_none(V1beta1DeviceAllocationResult)),
    ] = Field(
        default_factory=lambda: V1beta1DeviceAllocationResult(), exclude_if=_exclude_if
    )

    node_selector: Annotated[
        V1NodeSelector, BeforeValidator(_default_if_none(V1NodeSelector))
    ] = Field(
        default_factory=lambda: V1NodeSelector(),
        serialization_alias="nodeSelector",
        validation_alias=AliasChoices("node_selector", "nodeSelector"),
        exclude_if=_exclude_if,
    )

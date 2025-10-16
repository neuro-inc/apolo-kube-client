from __future__ import annotations
from pydantic import BaseModel, Field
from .v1beta2_capacity_requirements import V1beta2CapacityRequirements
from .v1beta2_device_selector import V1beta2DeviceSelector
from .v1beta2_device_toleration import V1beta2DeviceToleration

__all__ = ("V1beta2ExactDeviceRequest",)


class V1beta2ExactDeviceRequest(BaseModel):
    admin_access: bool | None = Field(default_factory=lambda: None, alias="adminAccess")

    allocation_mode: str | None = Field(
        default_factory=lambda: None, alias="allocationMode"
    )

    capacity: V1beta2CapacityRequirements = Field(
        default_factory=lambda: V1beta2CapacityRequirements(), alias="capacity"
    )

    count: int | None = Field(default_factory=lambda: None, alias="count")

    device_class_name: str | None = Field(
        default_factory=lambda: None, alias="deviceClassName"
    )

    selectors: list[V1beta2DeviceSelector] = Field(
        default_factory=lambda: [], alias="selectors"
    )

    tolerations: list[V1beta2DeviceToleration] = Field(
        default_factory=lambda: [], alias="tolerations"
    )

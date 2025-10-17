from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1beta2_capacity_requirements import V1beta2CapacityRequirements
from .v1beta2_device_selector import V1beta2DeviceSelector
from .v1beta2_device_toleration import V1beta2DeviceToleration

__all__ = ("V1beta2ExactDeviceRequest",)


class V1beta2ExactDeviceRequest(BaseModel):
    admin_access: bool | None = Field(
        default=None,
        serialization_alias="adminAccess",
        validation_alias=AliasChoices("admin_access", "adminAccess"),
    )

    allocation_mode: str | None = Field(
        default=None,
        serialization_alias="allocationMode",
        validation_alias=AliasChoices("allocation_mode", "allocationMode"),
    )

    capacity: V1beta2CapacityRequirements = Field(
        default_factory=lambda: V1beta2CapacityRequirements()
    )

    count: int | None = Field(default=None)

    device_class_name: str | None = Field(
        default=None,
        serialization_alias="deviceClassName",
        validation_alias=AliasChoices("device_class_name", "deviceClassName"),
    )

    selectors: list[V1beta2DeviceSelector] = Field(default=[])

    tolerations: list[V1beta2DeviceToleration] = Field(default=[])

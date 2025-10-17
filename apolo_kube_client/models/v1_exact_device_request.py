from pydantic import AliasChoices, BaseModel, Field
from .v1_capacity_requirements import V1CapacityRequirements
from .v1_device_selector import V1DeviceSelector
from .v1_device_toleration import V1DeviceToleration

__all__ = ("V1ExactDeviceRequest",)


class V1ExactDeviceRequest(BaseModel):
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

    capacity: V1CapacityRequirements = Field(
        default_factory=lambda: V1CapacityRequirements()
    )

    count: int | None = None

    device_class_name: str | None = Field(
        default=None,
        serialization_alias="deviceClassName",
        validation_alias=AliasChoices("device_class_name", "deviceClassName"),
    )

    selectors: list[V1DeviceSelector] = []

    tolerations: list[V1DeviceToleration] = []

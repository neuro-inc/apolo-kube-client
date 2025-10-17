from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1beta1_capacity_requirements import V1beta1CapacityRequirements
from .v1beta1_device_selector import V1beta1DeviceSelector
from .v1beta1_device_toleration import V1beta1DeviceToleration

__all__ = ("V1beta1DeviceSubRequest",)


class V1beta1DeviceSubRequest(BaseModel):
    allocation_mode: str | None = Field(
        default=None,
        serialization_alias="allocationMode",
        validation_alias=AliasChoices("allocation_mode", "allocationMode"),
    )

    capacity: V1beta1CapacityRequirements = Field(
        default_factory=lambda: V1beta1CapacityRequirements()
    )

    count: int | None = Field(default=None)

    device_class_name: str | None = Field(
        default=None,
        serialization_alias="deviceClassName",
        validation_alias=AliasChoices("device_class_name", "deviceClassName"),
    )

    name: str | None = Field(default=None)

    selectors: list[V1beta1DeviceSelector] = Field(default=[])

    tolerations: list[V1beta1DeviceToleration] = Field(default=[])

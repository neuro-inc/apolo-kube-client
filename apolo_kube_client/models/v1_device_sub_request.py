from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_capacity_requirements import V1CapacityRequirements
from .v1_device_selector import V1DeviceSelector
from .v1_device_toleration import V1DeviceToleration

__all__ = ("V1DeviceSubRequest",)


class V1DeviceSubRequest(BaseModel):
    allocation_mode: str | None = Field(
        default_factory=lambda: None, alias="allocationMode"
    )

    capacity: V1CapacityRequirements = Field(
        default_factory=lambda: V1CapacityRequirements()
    )

    count: int | None = Field(default_factory=lambda: None)

    device_class_name: str | None = Field(
        default_factory=lambda: None, alias="deviceClassName"
    )

    name: str | None = Field(default_factory=lambda: None)

    selectors: list[V1DeviceSelector] = Field(default_factory=lambda: [])

    tolerations: list[V1DeviceToleration] = Field(default_factory=lambda: [])

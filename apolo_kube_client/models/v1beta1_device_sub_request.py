from __future__ import annotations
from pydantic import BaseModel, Field
from .v1beta1_capacity_requirements import V1beta1CapacityRequirements
from .v1beta1_device_selector import V1beta1DeviceSelector
from .v1beta1_device_toleration import V1beta1DeviceToleration

__all__ = ("V1beta1DeviceSubRequest",)


class V1beta1DeviceSubRequest(BaseModel):
    allocation_mode: str | None = Field(
        default_factory=lambda: None, alias="allocationMode"
    )

    capacity: V1beta1CapacityRequirements = Field(
        default_factory=lambda: V1beta1CapacityRequirements(), alias="capacity"
    )

    count: int | None = Field(default_factory=lambda: None, alias="count")

    device_class_name: str | None = Field(
        default_factory=lambda: None, alias="deviceClassName"
    )

    name: str | None = Field(default_factory=lambda: None, alias="name")

    selectors: list[V1beta1DeviceSelector] = Field(
        default_factory=lambda: [], alias="selectors"
    )

    tolerations: list[V1beta1DeviceToleration] = Field(
        default_factory=lambda: [], alias="tolerations"
    )

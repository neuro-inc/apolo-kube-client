from __future__ import annotations
from pydantic import BaseModel, Field
from .v1beta2_device_toleration import V1beta2DeviceToleration

__all__ = ("V1beta2DeviceRequestAllocationResult",)


class V1beta2DeviceRequestAllocationResult(BaseModel):
    admin_access: bool | None = Field(default_factory=lambda: None, alias="adminAccess")

    binding_conditions: list[str] = Field(
        default_factory=lambda: [], alias="bindingConditions"
    )

    binding_failure_conditions: list[str] = Field(
        default_factory=lambda: [], alias="bindingFailureConditions"
    )

    consumed_capacity: dict[str, str] = Field(
        default_factory=lambda: {}, alias="consumedCapacity"
    )

    device: str | None = Field(default_factory=lambda: None, alias="device")

    driver: str | None = Field(default_factory=lambda: None, alias="driver")

    pool: str | None = Field(default_factory=lambda: None, alias="pool")

    request: str | None = Field(default_factory=lambda: None, alias="request")

    share_id: str | None = Field(default_factory=lambda: None, alias="shareID")

    tolerations: list[V1beta2DeviceToleration] = Field(
        default_factory=lambda: [], alias="tolerations"
    )

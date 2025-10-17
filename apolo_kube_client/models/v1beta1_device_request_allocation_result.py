from __future__ import annotations
from pydantic import BaseModel, Field
from .v1beta1_device_toleration import V1beta1DeviceToleration

__all__ = ("V1beta1DeviceRequestAllocationResult",)


class V1beta1DeviceRequestAllocationResult(BaseModel):
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

    device: str | None = Field(default_factory=lambda: None)

    driver: str | None = Field(default_factory=lambda: None)

    pool: str | None = Field(default_factory=lambda: None)

    request: str | None = Field(default_factory=lambda: None)

    share_id: str | None = Field(default_factory=lambda: None, alias="shareID")

    tolerations: list[V1beta1DeviceToleration] = Field(default_factory=lambda: [])

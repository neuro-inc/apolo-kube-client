from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1beta2_device_sub_request import V1beta2DeviceSubRequest
from .v1beta2_exact_device_request import V1beta2ExactDeviceRequest

__all__ = ("V1beta2DeviceRequest",)


class V1beta2DeviceRequest(BaseModel):
    exactly: V1beta2ExactDeviceRequest = Field(
        default_factory=lambda: V1beta2ExactDeviceRequest()
    )

    first_available: list[V1beta2DeviceSubRequest] = Field(
        default=[],
        serialization_alias="firstAvailable",
        validation_alias=AliasChoices("first_available", "firstAvailable"),
    )

    name: str | None = Field(default=None)

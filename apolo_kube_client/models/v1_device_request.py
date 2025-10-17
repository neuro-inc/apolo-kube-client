from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_device_sub_request import V1DeviceSubRequest
from .v1_exact_device_request import V1ExactDeviceRequest

__all__ = ("V1DeviceRequest",)


class V1DeviceRequest(BaseModel):
    exactly: V1ExactDeviceRequest = Field(
        default_factory=lambda: V1ExactDeviceRequest()
    )

    first_available: list[V1DeviceSubRequest] = Field(
        default=[],
        serialization_alias="firstAvailable",
        validation_alias=AliasChoices("first_available", "firstAvailable"),
    )

    name: str | None = Field(default=None)

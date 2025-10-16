from __future__ import annotations
from pydantic import BaseModel, Field
from .v1beta2_opaque_device_configuration import V1beta2OpaqueDeviceConfiguration

__all__ = ("V1beta2DeviceClaimConfiguration",)


class V1beta2DeviceClaimConfiguration(BaseModel):
    opaque: V1beta2OpaqueDeviceConfiguration = Field(
        default_factory=lambda: V1beta2OpaqueDeviceConfiguration(), alias="opaque"
    )

    requests: list[str] = Field(default_factory=lambda: [], alias="requests")

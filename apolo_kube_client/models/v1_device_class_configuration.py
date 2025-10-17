from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_opaque_device_configuration import V1OpaqueDeviceConfiguration

__all__ = ("V1DeviceClassConfiguration",)


class V1DeviceClassConfiguration(BaseModel):
    opaque: V1OpaqueDeviceConfiguration = Field(
        default_factory=lambda: V1OpaqueDeviceConfiguration()
    )

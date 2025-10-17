from __future__ import annotations
from pydantic import BaseModel, Field
from .v1beta2_cel_device_selector import V1beta2CELDeviceSelector

__all__ = ("V1beta2DeviceSelector",)


class V1beta2DeviceSelector(BaseModel):
    cel: V1beta2CELDeviceSelector = Field(
        default_factory=lambda: V1beta2CELDeviceSelector()
    )

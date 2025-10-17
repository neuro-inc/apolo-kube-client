from __future__ import annotations
from pydantic import BaseModel, Field
from .v1alpha3_cel_device_selector import V1alpha3CELDeviceSelector

__all__ = ("V1alpha3DeviceSelector",)


class V1alpha3DeviceSelector(BaseModel):
    cel: V1alpha3CELDeviceSelector = Field(
        default_factory=lambda: V1alpha3CELDeviceSelector()
    )

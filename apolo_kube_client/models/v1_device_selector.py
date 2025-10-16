from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_cel_device_selector import V1CELDeviceSelector

__all__ = ("V1DeviceSelector",)


class V1DeviceSelector(BaseModel):
    cel: V1CELDeviceSelector = Field(
        default_factory=lambda: V1CELDeviceSelector(), alias="cel"
    )

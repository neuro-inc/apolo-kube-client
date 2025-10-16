from __future__ import annotations
from pydantic import BaseModel, Field
from .v1beta1_cel_device_selector import V1beta1CELDeviceSelector

__all__ = ("V1beta1DeviceSelector",)


class V1beta1DeviceSelector(BaseModel):
    cel: V1beta1CELDeviceSelector = Field(
        default_factory=lambda: V1beta1CELDeviceSelector(), alias="cel"
    )

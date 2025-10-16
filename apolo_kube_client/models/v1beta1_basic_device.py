from __future__ import annotations

from pydantic import BaseModel, Field

from .v1beta1_device_attribute import V1beta1DeviceAttribute
from .v1beta1_device_capacity import V1beta1DeviceCapacity

__all__ = ("V1beta1BasicDevice",)


class V1beta1BasicDevice(BaseModel):
    attributes: dict[str, V1beta1DeviceAttribute] | None = Field(
        None, alias="attributes"
    )

    capacity: dict[str, V1beta1DeviceCapacity] | None = Field(None, alias="capacity")

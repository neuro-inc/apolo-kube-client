from __future__ import annotations

from pydantic import BaseModel, Field

from .v1alpha3_device_attribute import V1alpha3DeviceAttribute

__all__ = ("V1alpha3BasicDevice",)


class V1alpha3BasicDevice(BaseModel):
    attributes: dict[str, V1alpha3DeviceAttribute] | None = Field(
        None, alias="attributes"
    )

    capacity: dict[str, str] | None = Field(None, alias="capacity")

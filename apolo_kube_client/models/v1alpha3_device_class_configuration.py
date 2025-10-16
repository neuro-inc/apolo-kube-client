from __future__ import annotations

from pydantic import BaseModel, Field

from .v1alpha3_opaque_device_configuration import V1alpha3OpaqueDeviceConfiguration

__all__ = ("V1alpha3DeviceClassConfiguration",)


class V1alpha3DeviceClassConfiguration(BaseModel):
    opaque: V1alpha3OpaqueDeviceConfiguration | None = Field(None, alias="opaque")

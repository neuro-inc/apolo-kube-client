from __future__ import annotations

from pydantic import BaseModel, Field

from .v1alpha3_opaque_device_configuration import V1alpha3OpaqueDeviceConfiguration

__all__ = ("V1alpha3DeviceAllocationConfiguration",)


class V1alpha3DeviceAllocationConfiguration(BaseModel):
    opaque: V1alpha3OpaqueDeviceConfiguration | None = Field(None, alias="opaque")

    requests: list[str] | None = Field(None, alias="requests")

    source: str | None = Field(None, alias="source")

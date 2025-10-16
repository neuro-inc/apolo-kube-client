from __future__ import annotations

from pydantic import BaseModel, Field

from .v1beta1_opaque_device_configuration import V1beta1OpaqueDeviceConfiguration

__all__ = ("V1beta1DeviceAllocationConfiguration",)


class V1beta1DeviceAllocationConfiguration(BaseModel):
    opaque: V1beta1OpaqueDeviceConfiguration | None = Field(None, alias="opaque")

    requests: list[str] | None = Field(None, alias="requests")

    source: str | None = Field(None, alias="source")

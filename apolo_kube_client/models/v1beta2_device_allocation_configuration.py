from __future__ import annotations
from pydantic import BaseModel, Field
from .v1beta2_opaque_device_configuration import V1beta2OpaqueDeviceConfiguration

__all__ = ("V1beta2DeviceAllocationConfiguration",)


class V1beta2DeviceAllocationConfiguration(BaseModel):
    opaque: V1beta2OpaqueDeviceConfiguration = Field(
        default_factory=lambda: V1beta2OpaqueDeviceConfiguration(), alias="opaque"
    )

    requests: list[str] = Field(default_factory=lambda: [], alias="requests")

    source: str | None = Field(default_factory=lambda: None, alias="source")

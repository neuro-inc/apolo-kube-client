from __future__ import annotations
from pydantic import BaseModel, Field
from .v1beta1_opaque_device_configuration import V1beta1OpaqueDeviceConfiguration

__all__ = ("V1beta1DeviceAllocationConfiguration",)


class V1beta1DeviceAllocationConfiguration(BaseModel):
    opaque: V1beta1OpaqueDeviceConfiguration = Field(
        default_factory=lambda: V1beta1OpaqueDeviceConfiguration(), alias="opaque"
    )

    requests: list[str] = Field(default_factory=lambda: [], alias="requests")

    source: str | None = Field(default_factory=lambda: None, alias="source")

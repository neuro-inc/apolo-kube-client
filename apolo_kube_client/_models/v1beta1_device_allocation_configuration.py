from pydantic import BaseModel, Field
from .v1beta1_opaque_device_configuration import V1beta1OpaqueDeviceConfiguration

__all__ = ("V1beta1DeviceAllocationConfiguration",)


class V1beta1DeviceAllocationConfiguration(BaseModel):
    opaque: V1beta1OpaqueDeviceConfiguration = Field(
        default_factory=lambda: V1beta1OpaqueDeviceConfiguration()
    )

    requests: list[str] = []

    source: str | None = None

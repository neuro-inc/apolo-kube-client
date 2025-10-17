from pydantic import BaseModel, Field
from .v1beta2_opaque_device_configuration import V1beta2OpaqueDeviceConfiguration

__all__ = ("V1beta2DeviceClaimConfiguration",)


class V1beta2DeviceClaimConfiguration(BaseModel):
    opaque: V1beta2OpaqueDeviceConfiguration = Field(
        default_factory=lambda: V1beta2OpaqueDeviceConfiguration()
    )

    requests: list[str] = []

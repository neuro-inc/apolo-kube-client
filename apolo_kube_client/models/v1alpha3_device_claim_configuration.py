from pydantic import BaseModel, Field

from .v1alpha3_opaque_device_configuration import V1alpha3OpaqueDeviceConfiguration


class V1alpha3DeviceClaimConfiguration(BaseModel):
    opaque: V1alpha3OpaqueDeviceConfiguration | None = Field(None, alias="opaque")

    requests: list[str] | None = Field(None, alias="requests")

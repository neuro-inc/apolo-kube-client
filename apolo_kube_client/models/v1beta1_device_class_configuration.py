from pydantic import BaseModel, Field

from .v1beta1_opaque_device_configuration import V1beta1OpaqueDeviceConfiguration


class V1beta1DeviceClassConfiguration(BaseModel):
    opaque: V1beta1OpaqueDeviceConfiguration | None = Field(None, alias="opaque")

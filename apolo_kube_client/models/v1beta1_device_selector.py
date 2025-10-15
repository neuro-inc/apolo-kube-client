from pydantic import BaseModel, Field

from .v1beta1_c_e_l_device_selector import V1beta1CELDeviceSelector


class V1beta1DeviceSelector(BaseModel):
    cel: V1beta1CELDeviceSelector | None = Field(None, alias="cel")

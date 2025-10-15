from pydantic import BaseModel, Field

from .v1alpha3_c_e_l_device_selector import V1alpha3CELDeviceSelector


class V1alpha3DeviceSelector(BaseModel):
    cel: V1alpha3CELDeviceSelector | None = Field(None, alias="cel")

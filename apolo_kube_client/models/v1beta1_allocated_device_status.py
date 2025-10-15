from pydantic import BaseModel, Field

from .object import object
from .v1_condition import V1Condition
from .v1beta1_network_device_data import V1beta1NetworkDeviceData


class V1beta1AllocatedDeviceStatus(BaseModel):
    conditions: list[V1Condition] | None = Field(None, alias="conditions")

    data: object | None = Field(None, alias="data")

    device: str | None = Field(None, alias="device")

    driver: str | None = Field(None, alias="driver")

    network_data: V1beta1NetworkDeviceData | None = Field(None, alias="networkData")

    pool: str | None = Field(None, alias="pool")

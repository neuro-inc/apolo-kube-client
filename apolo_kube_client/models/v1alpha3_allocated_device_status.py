from pydantic import BaseModel, Field

from .object import object
from .v1_condition import V1Condition
from .v1alpha3_network_device_data import V1alpha3NetworkDeviceData


class V1alpha3AllocatedDeviceStatus(BaseModel):
    conditions: list[V1Condition] | None = Field(None, alias="conditions")

    data: object | None = Field(None, alias="data")

    device: str | None = Field(None, alias="device")

    driver: str | None = Field(None, alias="driver")

    network_data: V1alpha3NetworkDeviceData | None = Field(None, alias="networkData")

    pool: str | None = Field(None, alias="pool")

from __future__ import annotations

from pydantic import BaseModel, Field

from apolo_kube_client._typedefs import JsonType

from .v1_condition import V1Condition
from .v1alpha3_network_device_data import V1alpha3NetworkDeviceData

__all__ = ("V1alpha3AllocatedDeviceStatus",)


class V1alpha3AllocatedDeviceStatus(BaseModel):
    conditions: list[V1Condition] | None = Field(None, alias="conditions")

    data: JsonType | None = Field(None, alias="data")

    device: str | None = Field(None, alias="device")

    driver: str | None = Field(None, alias="driver")

    network_data: V1alpha3NetworkDeviceData | None = Field(None, alias="networkData")

    pool: str | None = Field(None, alias="pool")

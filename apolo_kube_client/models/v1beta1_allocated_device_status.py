from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_condition import V1Condition
from .v1beta1_network_device_data import V1beta1NetworkDeviceData
from apolo_kube_client._typedefs import JsonType

__all__ = ("V1beta1AllocatedDeviceStatus",)


class V1beta1AllocatedDeviceStatus(BaseModel):
    conditions: list[V1Condition] = Field(
        default_factory=lambda: [], alias="conditions"
    )

    data: JsonType = Field(default_factory=lambda: {}, alias="data")

    device: str | None = Field(default_factory=lambda: None, alias="device")

    driver: str | None = Field(default_factory=lambda: None, alias="driver")

    network_data: V1beta1NetworkDeviceData = Field(
        default_factory=lambda: V1beta1NetworkDeviceData(), alias="networkData"
    )

    pool: str | None = Field(default_factory=lambda: None, alias="pool")

    share_id: str | None = Field(default_factory=lambda: None, alias="shareID")

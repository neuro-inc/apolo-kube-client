from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_condition import V1Condition
from .v1beta2_network_device_data import V1beta2NetworkDeviceData
from apolo_kube_client._typedefs import JsonType

__all__ = ("V1beta2AllocatedDeviceStatus",)


class V1beta2AllocatedDeviceStatus(BaseModel):
    conditions: list[V1Condition] = Field(default_factory=lambda: [])

    data: JsonType = Field(default_factory=lambda: {})

    device: str | None = Field(default_factory=lambda: None)

    driver: str | None = Field(default_factory=lambda: None)

    network_data: V1beta2NetworkDeviceData = Field(
        default_factory=lambda: V1beta2NetworkDeviceData(), alias="networkData"
    )

    pool: str | None = Field(default_factory=lambda: None)

    share_id: str | None = Field(default_factory=lambda: None, alias="shareID")

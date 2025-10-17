from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_condition import V1Condition
from .v1_network_device_data import V1NetworkDeviceData
from apolo_kube_client._typedefs import JsonType

__all__ = ("V1AllocatedDeviceStatus",)


class V1AllocatedDeviceStatus(BaseModel):
    conditions: list[V1Condition] = Field(default=[])

    data: JsonType = Field(default={})

    device: str | None = Field(default=None)

    driver: str | None = Field(default=None)

    network_data: V1NetworkDeviceData = Field(
        default_factory=lambda: V1NetworkDeviceData(),
        serialization_alias="networkData",
        validation_alias=AliasChoices("network_data", "networkData"),
    )

    pool: str | None = Field(default=None)

    share_id: str | None = Field(
        default=None,
        serialization_alias="shareID",
        validation_alias=AliasChoices("share_id", "shareID"),
    )

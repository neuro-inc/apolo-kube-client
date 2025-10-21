from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .utils import _default_if_none
from .v1_condition import V1Condition
from .v1beta1_network_device_data import V1beta1NetworkDeviceData
from apolo_kube_client._typedefs import JsonType
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1beta1AllocatedDeviceStatus",)


class V1beta1AllocatedDeviceStatus(BaseModel):
    conditions: Annotated[
        list[V1Condition], BeforeValidator(_collection_if_none("[]"))
    ] = []

    data: JsonType = {}

    device: str | None = None

    driver: str | None = None

    network_data: Annotated[
        V1beta1NetworkDeviceData,
        BeforeValidator(_default_if_none(V1beta1NetworkDeviceData)),
    ] = Field(
        default_factory=lambda: V1beta1NetworkDeviceData(),
        serialization_alias="networkData",
        validation_alias=AliasChoices("network_data", "networkData"),
    )

    pool: str | None = None

    share_id: str | None = Field(
        default=None,
        serialization_alias="shareID",
        validation_alias=AliasChoices("share_id", "shareID"),
    )

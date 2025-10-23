from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .utils import _default_if_none
from .utils import _exclude_if
from .v1_condition import V1Condition
from .v1beta1_network_device_data import V1beta1NetworkDeviceData
from apolo_kube_client._typedefs import JsonType
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1beta1AllocatedDeviceStatus",)


class V1beta1AllocatedDeviceStatus(BaseModel):
    conditions: Annotated[
        list[V1Condition], BeforeValidator(_collection_if_none("[]"))
    ] = Field(default=[], exclude_if=_exclude_if)

    data: JsonType = Field(default={}, exclude_if=_exclude_if)

    device: str | None = Field(default=None, exclude_if=_exclude_if)

    driver: str | None = Field(default=None, exclude_if=_exclude_if)

    network_data: Annotated[
        V1beta1NetworkDeviceData,
        BeforeValidator(_default_if_none(V1beta1NetworkDeviceData)),
    ] = Field(
        default_factory=lambda: V1beta1NetworkDeviceData(),
        serialization_alias="networkData",
        validation_alias=AliasChoices("network_data", "networkData"),
        exclude_if=_exclude_if,
    )

    pool: str | None = Field(default=None, exclude_if=_exclude_if)

    share_id: str | None = Field(
        default=None,
        serialization_alias="shareID",
        validation_alias=AliasChoices("share_id", "shareID"),
        exclude_if=_exclude_if,
    )

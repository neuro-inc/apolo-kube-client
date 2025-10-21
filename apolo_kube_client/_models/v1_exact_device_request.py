from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .utils import _default_if_none
from .v1_capacity_requirements import V1CapacityRequirements
from .v1_device_selector import V1DeviceSelector
from .v1_device_toleration import V1DeviceToleration
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1ExactDeviceRequest",)


class V1ExactDeviceRequest(BaseModel):
    admin_access: bool | None = Field(
        default=None,
        serialization_alias="adminAccess",
        validation_alias=AliasChoices("admin_access", "adminAccess"),
    )

    allocation_mode: str | None = Field(
        default=None,
        serialization_alias="allocationMode",
        validation_alias=AliasChoices("allocation_mode", "allocationMode"),
    )

    capacity: Annotated[
        V1CapacityRequirements,
        BeforeValidator(_default_if_none(V1CapacityRequirements)),
    ] = Field(default_factory=lambda: V1CapacityRequirements())

    count: int | None = None

    device_class_name: str | None = Field(
        default=None,
        serialization_alias="deviceClassName",
        validation_alias=AliasChoices("device_class_name", "deviceClassName"),
    )

    selectors: Annotated[
        list[V1DeviceSelector], BeforeValidator(_collection_if_none("[]"))
    ] = []

    tolerations: Annotated[
        list[V1DeviceToleration], BeforeValidator(_collection_if_none("[]"))
    ] = []

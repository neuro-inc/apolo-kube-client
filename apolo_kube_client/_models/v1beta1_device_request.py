from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .utils import _default_if_none
from .v1beta1_capacity_requirements import V1beta1CapacityRequirements
from .v1beta1_device_selector import V1beta1DeviceSelector
from .v1beta1_device_sub_request import V1beta1DeviceSubRequest
from .v1beta1_device_toleration import V1beta1DeviceToleration
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1beta1DeviceRequest",)


class V1beta1DeviceRequest(BaseModel):
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
        V1beta1CapacityRequirements,
        BeforeValidator(_default_if_none(V1beta1CapacityRequirements)),
    ] = Field(default_factory=lambda: V1beta1CapacityRequirements())

    count: int | None = None

    device_class_name: str | None = Field(
        default=None,
        serialization_alias="deviceClassName",
        validation_alias=AliasChoices("device_class_name", "deviceClassName"),
    )

    first_available: Annotated[
        list[V1beta1DeviceSubRequest], BeforeValidator(_collection_if_none("[]"))
    ] = Field(
        default=[],
        serialization_alias="firstAvailable",
        validation_alias=AliasChoices("first_available", "firstAvailable"),
    )

    name: str | None = None

    selectors: Annotated[
        list[V1beta1DeviceSelector], BeforeValidator(_collection_if_none("[]"))
    ] = []

    tolerations: Annotated[
        list[V1beta1DeviceToleration], BeforeValidator(_collection_if_none("[]"))
    ] = []

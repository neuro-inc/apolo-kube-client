from pydantic import AliasChoices, BaseModel, Field
from .base import _default_if_none
from .v1beta2_capacity_requirements import V1beta2CapacityRequirements
from .v1beta2_device_selector import V1beta2DeviceSelector
from .v1beta2_device_toleration import V1beta2DeviceToleration
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1beta2DeviceSubRequest",)


class V1beta2DeviceSubRequest(BaseModel):
    allocation_mode: str | None = Field(
        default=None,
        serialization_alias="allocationMode",
        validation_alias=AliasChoices("allocation_mode", "allocationMode"),
    )

    capacity: Annotated[
        V1beta2CapacityRequirements,
        BeforeValidator(_default_if_none(V1beta2CapacityRequirements)),
    ] = Field(default_factory=lambda: V1beta2CapacityRequirements())

    count: int | None = None

    device_class_name: str | None = Field(
        default=None,
        serialization_alias="deviceClassName",
        validation_alias=AliasChoices("device_class_name", "deviceClassName"),
    )

    name: str | None = None

    selectors: list[V1beta2DeviceSelector] = []

    tolerations: list[V1beta2DeviceToleration] = []

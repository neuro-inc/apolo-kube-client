from pydantic import AliasChoices, BaseModel, Field
from .base import _default_if_none
from .v1beta2_device_sub_request import V1beta2DeviceSubRequest
from .v1beta2_exact_device_request import V1beta2ExactDeviceRequest
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1beta2DeviceRequest",)


class V1beta2DeviceRequest(BaseModel):
    exactly: Annotated[
        V1beta2ExactDeviceRequest,
        BeforeValidator(_default_if_none(V1beta2ExactDeviceRequest)),
    ] = Field(default_factory=lambda: V1beta2ExactDeviceRequest())

    first_available: list[V1beta2DeviceSubRequest] = Field(
        default=[],
        serialization_alias="firstAvailable",
        validation_alias=AliasChoices("first_available", "firstAvailable"),
    )

    name: str | None = None

from pydantic import BaseModel, Field
from .base import _default_if_none
from .v1beta2_opaque_device_configuration import V1beta2OpaqueDeviceConfiguration
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1beta2DeviceClaimConfiguration",)


class V1beta2DeviceClaimConfiguration(BaseModel):
    opaque: Annotated[
        V1beta2OpaqueDeviceConfiguration,
        BeforeValidator(_default_if_none(V1beta2OpaqueDeviceConfiguration)),
    ] = Field(default_factory=lambda: V1beta2OpaqueDeviceConfiguration())

    requests: list[str] = []

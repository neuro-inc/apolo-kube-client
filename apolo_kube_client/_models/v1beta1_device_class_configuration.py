from pydantic import BaseModel, Field
from .base import _default_if_none
from .v1beta1_opaque_device_configuration import V1beta1OpaqueDeviceConfiguration
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1beta1DeviceClassConfiguration",)


class V1beta1DeviceClassConfiguration(BaseModel):
    opaque: Annotated[
        V1beta1OpaqueDeviceConfiguration,
        BeforeValidator(_default_if_none(V1beta1OpaqueDeviceConfiguration)),
    ] = Field(default_factory=lambda: V1beta1OpaqueDeviceConfiguration())

from pydantic import BaseModel, Field
from .utils import _default_if_none
from .utils import _exclude_if
from .v1beta2_opaque_device_configuration import V1beta2OpaqueDeviceConfiguration
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1beta2DeviceClassConfiguration",)


class V1beta2DeviceClassConfiguration(BaseModel):
    opaque: Annotated[
        V1beta2OpaqueDeviceConfiguration,
        BeforeValidator(_default_if_none(V1beta2OpaqueDeviceConfiguration)),
    ] = Field(
        default_factory=lambda: V1beta2OpaqueDeviceConfiguration(),
        exclude_if=_exclude_if,
    )

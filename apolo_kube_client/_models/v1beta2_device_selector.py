from pydantic import BaseModel, Field
from .base import _default_if_none
from .v1beta2_cel_device_selector import V1beta2CELDeviceSelector
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1beta2DeviceSelector",)


class V1beta2DeviceSelector(BaseModel):
    cel: Annotated[
        V1beta2CELDeviceSelector,
        BeforeValidator(_default_if_none(V1beta2CELDeviceSelector)),
    ] = Field(default_factory=lambda: V1beta2CELDeviceSelector())

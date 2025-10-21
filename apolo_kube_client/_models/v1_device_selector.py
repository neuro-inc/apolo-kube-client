from pydantic import BaseModel, Field
from .base import _default_if_none
from .v1_cel_device_selector import V1CELDeviceSelector
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1DeviceSelector",)


class V1DeviceSelector(BaseModel):
    cel: Annotated[
        V1CELDeviceSelector, BeforeValidator(_default_if_none(V1CELDeviceSelector))
    ] = Field(default_factory=lambda: V1CELDeviceSelector())

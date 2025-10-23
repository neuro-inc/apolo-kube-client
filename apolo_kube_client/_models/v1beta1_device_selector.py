from pydantic import BaseModel, Field
from .utils import _default_if_none
from .utils import _exclude_if
from .v1beta1_cel_device_selector import V1beta1CELDeviceSelector
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1beta1DeviceSelector",)


class V1beta1DeviceSelector(BaseModel):
    cel: Annotated[
        V1beta1CELDeviceSelector,
        BeforeValidator(_default_if_none(V1beta1CELDeviceSelector)),
    ] = Field(
        default_factory=lambda: V1beta1CELDeviceSelector(), exclude_if=_exclude_if
    )

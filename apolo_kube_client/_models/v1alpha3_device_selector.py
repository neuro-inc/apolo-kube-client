from pydantic import BaseModel, Field
from .utils import _default_if_none
from .utils import _exclude_if
from .v1alpha3_cel_device_selector import V1alpha3CELDeviceSelector
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1alpha3DeviceSelector",)


class V1alpha3DeviceSelector(BaseModel):
    cel: Annotated[
        V1alpha3CELDeviceSelector,
        BeforeValidator(_default_if_none(V1alpha3CELDeviceSelector)),
    ] = Field(
        default_factory=lambda: V1alpha3CELDeviceSelector(), exclude_if=_exclude_if
    )

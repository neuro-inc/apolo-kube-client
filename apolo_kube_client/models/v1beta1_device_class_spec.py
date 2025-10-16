from __future__ import annotations

from pydantic import BaseModel, Field

from .v1beta1_device_class_configuration import V1beta1DeviceClassConfiguration
from .v1beta1_device_selector import V1beta1DeviceSelector

__all__ = ("V1beta1DeviceClassSpec",)


class V1beta1DeviceClassSpec(BaseModel):
    config: list[V1beta1DeviceClassConfiguration] | None = Field(None, alias="config")

    selectors: list[V1beta1DeviceSelector] | None = Field(None, alias="selectors")

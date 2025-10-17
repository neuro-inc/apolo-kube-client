from __future__ import annotations
from pydantic import BaseModel, Field
from .v1beta2_device_class_configuration import V1beta2DeviceClassConfiguration
from .v1beta2_device_selector import V1beta2DeviceSelector

__all__ = ("V1beta2DeviceClassSpec",)


class V1beta2DeviceClassSpec(BaseModel):
    config: list[V1beta2DeviceClassConfiguration] = Field(default_factory=lambda: [])

    extended_resource_name: str | None = Field(
        default_factory=lambda: None, alias="extendedResourceName"
    )

    selectors: list[V1beta2DeviceSelector] = Field(default_factory=lambda: [])

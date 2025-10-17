from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_device_class_configuration import V1DeviceClassConfiguration
from .v1_device_selector import V1DeviceSelector

__all__ = ("V1DeviceClassSpec",)


class V1DeviceClassSpec(BaseModel):
    config: list[V1DeviceClassConfiguration] = Field(default_factory=lambda: [])

    extended_resource_name: str | None = Field(
        default_factory=lambda: None, alias="extendedResourceName"
    )

    selectors: list[V1DeviceSelector] = Field(default_factory=lambda: [])

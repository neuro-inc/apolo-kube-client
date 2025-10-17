from __future__ import annotations
from pydantic import BaseModel, Field
from .v1alpha3_device_selector import V1alpha3DeviceSelector

__all__ = ("V1alpha3DeviceTaintSelector",)


class V1alpha3DeviceTaintSelector(BaseModel):
    device: str | None = Field(default_factory=lambda: None)

    device_class_name: str | None = Field(
        default_factory=lambda: None, alias="deviceClassName"
    )

    driver: str | None = Field(default_factory=lambda: None)

    pool: str | None = Field(default_factory=lambda: None)

    selectors: list[V1alpha3DeviceSelector] = Field(default_factory=lambda: [])

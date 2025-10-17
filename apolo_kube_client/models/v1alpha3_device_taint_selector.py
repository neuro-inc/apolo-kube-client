from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1alpha3_device_selector import V1alpha3DeviceSelector

__all__ = ("V1alpha3DeviceTaintSelector",)


class V1alpha3DeviceTaintSelector(BaseModel):
    device: str | None = Field(default=None)

    device_class_name: str | None = Field(
        default=None,
        serialization_alias="deviceClassName",
        validation_alias=AliasChoices("device_class_name", "deviceClassName"),
    )

    driver: str | None = Field(default=None)

    pool: str | None = Field(default=None)

    selectors: list[V1alpha3DeviceSelector] = Field(default=[])

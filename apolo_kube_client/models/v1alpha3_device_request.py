from __future__ import annotations

from pydantic import BaseModel, Field

from .v1alpha3_device_selector import V1alpha3DeviceSelector

__all__ = ("V1alpha3DeviceRequest",)


class V1alpha3DeviceRequest(BaseModel):
    admin_access: bool | None = Field(None, alias="adminAccess")

    allocation_mode: str | None = Field(None, alias="allocationMode")

    count: int | None = Field(None, alias="count")

    device_class_name: str | None = Field(None, alias="deviceClassName")

    name: str | None = Field(None, alias="name")

    selectors: list[V1alpha3DeviceSelector] | None = Field(None, alias="selectors")

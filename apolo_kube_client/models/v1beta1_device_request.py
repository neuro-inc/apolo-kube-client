from pydantic import BaseModel, Field

from .v1beta1_device_selector import V1beta1DeviceSelector


class V1beta1DeviceRequest(BaseModel):
    admin_access: bool | None = Field(None, alias="adminAccess")

    allocation_mode: str | None = Field(None, alias="allocationMode")

    count: int | None = Field(None, alias="count")

    device_class_name: str | None = Field(None, alias="deviceClassName")

    name: str | None = Field(None, alias="name")

    selectors: list[V1beta1DeviceSelector] | None = Field(None, alias="selectors")

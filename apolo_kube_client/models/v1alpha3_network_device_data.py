from __future__ import annotations

from pydantic import BaseModel, Field

__all__ = ("V1alpha3NetworkDeviceData",)


class V1alpha3NetworkDeviceData(BaseModel):
    hardware_address: str | None = Field(None, alias="hardwareAddress")

    interface_name: str | None = Field(None, alias="interfaceName")

    ips: list[str] | None = Field(None, alias="ips")

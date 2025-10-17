from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1NetworkDeviceData",)


class V1NetworkDeviceData(BaseModel):
    hardware_address: str | None = Field(
        default_factory=lambda: None, alias="hardwareAddress"
    )

    interface_name: str | None = Field(
        default_factory=lambda: None, alias="interfaceName"
    )

    ips: list[str] = Field(default_factory=lambda: [])

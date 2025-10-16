from __future__ import annotations
from pydantic import BaseModel, Field
from .v1beta2_device_claim import V1beta2DeviceClaim

__all__ = ("V1beta2ResourceClaimSpec",)


class V1beta2ResourceClaimSpec(BaseModel):
    devices: V1beta2DeviceClaim = Field(
        default_factory=lambda: V1beta2DeviceClaim(), alias="devices"
    )

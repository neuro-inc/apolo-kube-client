from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_device_claim import V1DeviceClaim

__all__ = ("V1ResourceClaimSpec",)


class V1ResourceClaimSpec(BaseModel):
    devices: V1DeviceClaim = Field(default_factory=lambda: V1DeviceClaim())

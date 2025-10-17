from __future__ import annotations
from pydantic import BaseModel, Field
from .v1beta1_device_claim import V1beta1DeviceClaim

__all__ = ("V1beta1ResourceClaimSpec",)


class V1beta1ResourceClaimSpec(BaseModel):
    devices: V1beta1DeviceClaim = Field(default_factory=lambda: V1beta1DeviceClaim())

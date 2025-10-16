from __future__ import annotations

from pydantic import BaseModel, Field

from .v1alpha3_device_claim import V1alpha3DeviceClaim

__all__ = ("V1alpha3ResourceClaimSpec",)


class V1alpha3ResourceClaimSpec(BaseModel):
    devices: V1alpha3DeviceClaim | None = Field(None, alias="devices")

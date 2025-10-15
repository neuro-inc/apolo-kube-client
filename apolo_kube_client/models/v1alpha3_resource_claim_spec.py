from pydantic import BaseModel, Field

from .v1alpha3_device_claim import V1alpha3DeviceClaim


class V1alpha3ResourceClaimSpec(BaseModel):
    devices: V1alpha3DeviceClaim | None = Field(None, alias="devices")

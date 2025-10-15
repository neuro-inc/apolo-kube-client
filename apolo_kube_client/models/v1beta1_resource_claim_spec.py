from pydantic import BaseModel, Field

from .v1beta1_device_claim import V1beta1DeviceClaim


class V1beta1ResourceClaimSpec(BaseModel):
    devices: V1beta1DeviceClaim | None = Field(None, alias="devices")

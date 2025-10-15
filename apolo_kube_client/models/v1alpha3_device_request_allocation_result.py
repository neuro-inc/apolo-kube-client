from pydantic import BaseModel, Field


class V1alpha3DeviceRequestAllocationResult(BaseModel):
    admin_access: bool | None = Field(None, alias="adminAccess")

    device: str | None = Field(None, alias="device")

    driver: str | None = Field(None, alias="driver")

    pool: str | None = Field(None, alias="pool")

    request: str | None = Field(None, alias="request")

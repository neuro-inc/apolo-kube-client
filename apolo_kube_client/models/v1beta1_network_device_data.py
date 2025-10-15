from pydantic import BaseModel, Field


class V1beta1NetworkDeviceData(BaseModel):
    hardware_address: str | None = Field(None, alias="hardwareAddress")

    interface_name: str | None = Field(None, alias="interfaceName")

    ips: list[str] | None = Field(None, alias="ips")

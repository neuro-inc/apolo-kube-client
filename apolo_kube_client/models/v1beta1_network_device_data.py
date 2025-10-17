from pydantic import AliasChoices, BaseModel, Field


__all__ = ("V1beta1NetworkDeviceData",)


class V1beta1NetworkDeviceData(BaseModel):
    hardware_address: str | None = Field(
        default=None,
        serialization_alias="hardwareAddress",
        validation_alias=AliasChoices("hardware_address", "hardwareAddress"),
    )

    interface_name: str | None = Field(
        default=None,
        serialization_alias="interfaceName",
        validation_alias=AliasChoices("interface_name", "interfaceName"),
    )

    ips: list[str] = []

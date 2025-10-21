from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1NetworkDeviceData",)


class V1NetworkDeviceData(BaseModel):
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

    ips: Annotated[list[str], BeforeValidator(_collection_if_none("[]"))] = []

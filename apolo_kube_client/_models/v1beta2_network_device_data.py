from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .utils import _exclude_if
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1beta2NetworkDeviceData",)


class V1beta2NetworkDeviceData(BaseModel):
    hardware_address: str | None = Field(
        default=None,
        serialization_alias="hardwareAddress",
        validation_alias=AliasChoices("hardware_address", "hardwareAddress"),
        exclude_if=_exclude_if,
    )

    interface_name: str | None = Field(
        default=None,
        serialization_alias="interfaceName",
        validation_alias=AliasChoices("interface_name", "interfaceName"),
        exclude_if=_exclude_if,
    )

    ips: Annotated[list[str], BeforeValidator(_collection_if_none("[]"))] = Field(
        default=[], exclude_if=_exclude_if
    )

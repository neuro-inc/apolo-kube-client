from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .utils import _exclude_if
from .v1alpha3_device_selector import V1alpha3DeviceSelector
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1alpha3DeviceTaintSelector",)


class V1alpha3DeviceTaintSelector(BaseModel):
    device: str | None = Field(default=None, exclude_if=_exclude_if)

    device_class_name: str | None = Field(
        default=None,
        serialization_alias="deviceClassName",
        validation_alias=AliasChoices("device_class_name", "deviceClassName"),
        exclude_if=_exclude_if,
    )

    driver: str | None = Field(default=None, exclude_if=_exclude_if)

    pool: str | None = Field(default=None, exclude_if=_exclude_if)

    selectors: Annotated[
        list[V1alpha3DeviceSelector], BeforeValidator(_collection_if_none("[]"))
    ] = Field(default=[], exclude_if=_exclude_if)

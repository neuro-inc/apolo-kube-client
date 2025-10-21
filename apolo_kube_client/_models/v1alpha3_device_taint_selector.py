from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .v1alpha3_device_selector import V1alpha3DeviceSelector
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1alpha3DeviceTaintSelector",)


class V1alpha3DeviceTaintSelector(BaseModel):
    device: str | None = None

    device_class_name: str | None = Field(
        default=None,
        serialization_alias="deviceClassName",
        validation_alias=AliasChoices("device_class_name", "deviceClassName"),
    )

    driver: str | None = None

    pool: str | None = None

    selectors: Annotated[
        list[V1alpha3DeviceSelector], BeforeValidator(_collection_if_none("[]"))
    ] = []

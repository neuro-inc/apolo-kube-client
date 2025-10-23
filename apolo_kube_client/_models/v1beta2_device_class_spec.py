from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .utils import _exclude_if
from .v1beta2_device_class_configuration import V1beta2DeviceClassConfiguration
from .v1beta2_device_selector import V1beta2DeviceSelector
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1beta2DeviceClassSpec",)


class V1beta2DeviceClassSpec(BaseModel):
    config: Annotated[
        list[V1beta2DeviceClassConfiguration],
        BeforeValidator(_collection_if_none("[]")),
    ] = Field(default=[], exclude_if=_exclude_if)

    extended_resource_name: str | None = Field(
        default=None,
        serialization_alias="extendedResourceName",
        validation_alias=AliasChoices("extended_resource_name", "extendedResourceName"),
        exclude_if=_exclude_if,
    )

    selectors: Annotated[
        list[V1beta2DeviceSelector], BeforeValidator(_collection_if_none("[]"))
    ] = Field(default=[], exclude_if=_exclude_if)

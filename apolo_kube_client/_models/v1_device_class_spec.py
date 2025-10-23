from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .utils import _exclude_if
from .v1_device_class_configuration import V1DeviceClassConfiguration
from .v1_device_selector import V1DeviceSelector
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1DeviceClassSpec",)


class V1DeviceClassSpec(BaseModel):
    config: Annotated[
        list[V1DeviceClassConfiguration], BeforeValidator(_collection_if_none("[]"))
    ] = Field(default=[], exclude_if=_exclude_if)

    extended_resource_name: str | None = Field(
        default=None,
        serialization_alias="extendedResourceName",
        validation_alias=AliasChoices("extended_resource_name", "extendedResourceName"),
        exclude_if=_exclude_if,
    )

    selectors: Annotated[
        list[V1DeviceSelector], BeforeValidator(_collection_if_none("[]"))
    ] = Field(default=[], exclude_if=_exclude_if)

from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .v1beta1_device_class_configuration import V1beta1DeviceClassConfiguration
from .v1beta1_device_selector import V1beta1DeviceSelector
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1beta1DeviceClassSpec",)


class V1beta1DeviceClassSpec(BaseModel):
    config: Annotated[
        list[V1beta1DeviceClassConfiguration],
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    extended_resource_name: str | None = Field(
        default=None,
        serialization_alias="extendedResourceName",
        validation_alias=AliasChoices("extended_resource_name", "extendedResourceName"),
    )

    selectors: Annotated[
        list[V1beta1DeviceSelector], BeforeValidator(_collection_if_none("[]"))
    ] = []

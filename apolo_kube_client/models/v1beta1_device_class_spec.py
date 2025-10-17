from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1beta1_device_class_configuration import V1beta1DeviceClassConfiguration
from .v1beta1_device_selector import V1beta1DeviceSelector

__all__ = ("V1beta1DeviceClassSpec",)


class V1beta1DeviceClassSpec(BaseModel):
    config: list[V1beta1DeviceClassConfiguration] = Field(default=[])

    extended_resource_name: str | None = Field(
        default=None,
        serialization_alias="extendedResourceName",
        validation_alias=AliasChoices("extended_resource_name", "extendedResourceName"),
    )

    selectors: list[V1beta1DeviceSelector] = Field(default=[])

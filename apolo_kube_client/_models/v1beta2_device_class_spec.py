from pydantic import AliasChoices, BaseModel, Field
from .v1beta2_device_class_configuration import V1beta2DeviceClassConfiguration
from .v1beta2_device_selector import V1beta2DeviceSelector

__all__ = ("V1beta2DeviceClassSpec",)


class V1beta2DeviceClassSpec(BaseModel):
    config: list[V1beta2DeviceClassConfiguration] = []

    extended_resource_name: str | None = Field(
        default=None,
        serialization_alias="extendedResourceName",
        validation_alias=AliasChoices("extended_resource_name", "extendedResourceName"),
    )

    selectors: list[V1beta2DeviceSelector] = []
